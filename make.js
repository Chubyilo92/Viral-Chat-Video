const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,HeadingLevel,Table,TableRow,TableCell,WidthType,ShadingType,AlignmentType,LevelFormat,PageBreak,BorderStyle}=require('docx');
const P=JSON.parse(fs.readFileSync('plan.json','utf8'));
const W=9026; // A4 content width in DXA (1440 margins)
const FONT="Arial";
const t=(s,o={})=>new TextRun({text:s,font:FONT,...o});
const para=(runs,o={})=>new Paragraph({children:Array.isArray(runs)?runs:[t(runs)],spacing:{after:120},...o});
const h1=s=>new Paragraph({heading:HeadingLevel.HEADING_1,children:[t(s)],spacing:{before:240,after:160}});
const h2=s=>new Paragraph({heading:HeadingLevel.HEADING_2,children:[t(s)],spacing:{before:240,after:120}});
const h3=s=>new Paragraph({heading:HeadingLevel.HEADING_3,children:[t(s)],spacing:{before:200,after:100},keepNext:true});
const bullet=(runs)=>new Paragraph({numbering:{reference:"bul",level:0},children:Array.isArray(runs)?runs:[t(runs)],spacing:{after:60}});
let numRef=0; const numbered=[];
function newList(){numRef++; const r="num"+numRef; numbered.push(r); return r;}
const num=(ref,runs)=>new Paragraph({numbering:{reference:ref,level:0},children:Array.isArray(runs)?runs:[t(runs)],spacing:{after:80}});
const border={style:BorderStyle.SINGLE,size:4,color:"D9CCD2"};
const borders={top:border,bottom:border,left:border,right:border};
function table(cols,rows,header=true){
  const mk=(cells,isH)=>new TableRow({tableHeader:isH,children:cells.map((c,i)=>new TableCell({borders,width:{size:cols[i],type:WidthType.DXA},
     shading:isH?{fill:"F6E3EA",type:ShadingType.CLEAR,color:"auto"}:undefined,margins:{top:60,bottom:60,left:100,right:100},
     children:[new Paragraph({children:[t(String(c),isH?{bold:true}:{})]})]}))});
  return new Table({width:{size:W,type:WidthType.DXA},columnWidths:cols,rows:[...(header?[mk(rows[0],true)]:[]),...rows.slice(header?1:0).map(r=>mk(r,false))]});
}
function kv(rows){ // 2-col label/value
  const cols=[2300,W-2300];
  return new Table({width:{size:W,type:WidthType.DXA},columnWidths:cols,rows:rows.map(([k,v])=>new TableRow({children:[
    new TableCell({borders,width:{size:cols[0],type:WidthType.DXA},shading:{fill:"FBF3F6",type:ShadingType.CLEAR,color:"auto"},margins:{top:60,bottom:60,left:100,right:100},children:[new Paragraph({children:[t(k,{bold:true})]})]}),
    new TableCell({borders,width:{size:cols[1],type:WidthType.DXA},margins:{top:60,bottom:60,left:100,right:100},children:[new Paragraph({children:[t(v)]})]})]}))});
}
const kids=[];
kids.push(new Paragraph({heading:HeadingLevel.TITLE,children:[t("CoupleIn twist reels: filming guide")]}));
kids.push(para("All 60 videos for the month. What to set up, what to film, and on whose login, in the exact order to do it."));
kids.push(para([t("How every video works: ",{bold:true}),t("a fake Instagram DM fight that looks like cheating, then 5 to 8 seconds of your screen recording, then the twist in the DMs, then the CoupleIn end card. Your recording is only the middle part. I make the DMs, captions, twist and end card.")]));
kids.push(para([t("The one rule for every clip: ",{bold:true}),t("film on the ANGRY person's login. The clip shows what they find or do. It never shows the answer. (Two exceptions, V44 and V106, are marked where they come up.)")]));

kids.push(h1("Step 0: Before you start"));
let L=newList();
[
 "Two CoupleIn logins, linked as a couple: Jay and Ella. Plain avatars (initials or a colour), no real people's photos.",
 "Two phones is easiest (one logged in as Jay, one as Ella). One phone also works: log out and in when this guide says to switch.",
 "Turn on Do Not Disturb, so no notifications appear in the recordings.",
 "Use the phone's own screen recorder. Hold the phone upright.",
 "What \u201chold\u201d means: stop moving and take your finger off the screen while you count to 5. Nothing needs opening unless the step says so. The still moments are what go in the video, and they're how I find where each clip starts and ends.",
 "Keep each recording under 3 minutes. Don't worry about file size or naming. I handle both.",
 "If something in this guide doesn't exist in the app (a mood, event notes, a repeat option), skip that item and tell me. I'll rewrite the video around what the app has.",
].forEach(s=>kids.push(num(L,s)));

kids.push(h1("Step 1: Set up Ella's login"));
kids.push(h2("1a. Ella's wishlist (add all 16)"));
kids.push(table([W-1800,1800],[["Wishlist item (type it exactly)","Points"],...P.wish.map(([a,b])=>[a,"+"+b])]));
kids.push(para(""));
kids.push(h2("1b. Calendar events Ella creates"));
const calRows=c=>[c.title,c.when,c.repeat,c.note||"—",c.id];
kids.push(table([2600,2300,1700,1600,826],[["Title (type exactly)","When","Repeat","Note","For"],...P.cal.filter(c=>c.creator=="Ella").map(calRows)]));
kids.push(para(""));
kids.push(para([t("Don't set a mood yet. ",{bold:true}),t("Moods are set one at a time during Step 3 (recording J3).")]));

kids.push(h1("Step 2: Set up Jay's login"));
kids.push(h2("2a. Calendar events Jay creates"));
kids.push(table([2600,2300,1700,1600,826],[["Title (type exactly)","When","Repeat","Note","For"],...P.cal.filter(c=>c.creator=="Jay").map(calRows)]));
kids.push(para(""));
kids.push(para("Jay adds nothing to Brownies. His part in Brownies is tapping “I did this” on Ella's items while recording."));

const recBlock=(r)=>{
  kids.push(h2(`Recording ${r.code}: ${r.title}`));
  const L=newList();
  r.items.forEach(it=>kids.push(num(L,[t(`[${it.id}] `,{bold:true}),t(it.step)])));
};
kids.push(h1("Step 3: Record on Jay's login"));
kids.push(para("Log in as Jay. Start the screen recorder, do the items in order, then stop. One recording per heading. J3 is 4 very short recordings."));
P.recs.filter(r=>r.phone=="Jay").forEach(recBlock);
kids.push(h1("Step 4: Record on Ella's login"));
kids.push(para("Log in as Ella. Same routine."));
P.recs.filter(r=>r.phone=="Ella").forEach(recBlock);

kids.push(h1("Step 5: Take 2 photos"));
L=newList();
kids.push(num(L,[t("[V01] ",{bold:true}),t("A cat. Any cat, a normal phone photo.")]));
kids.push(num(L,[t("[V33] ",{bold:true}),t("A sausage roll, in its paper bag if possible.")]));

kids.push(h1("Step 6: Send it to me"));
L=newList();
kids.push(num(L,"Attach all the recordings (J1, J2, the four J3s, J4, E1, E2, E3 = 11 files) and the 2 photos in the chat. That's 13 files, under the 20-per-chat limit. Write the codes in the same order as you attach them, e.g. \u201cJ1, J2, J3a, J3b, J3c, J3d, J4, E1, E2, E3\u201d."));
kids.push(num(L,"Paste your GitHub key (Contents: read and write, Coupleinsocial only, 90-day expiry)."));
kids.push(num(L,"That's it. I cut the clips, build the videos, check them and show you. Nothing posts until you've seen it."));

kids.push(new Paragraph({children:[new PageBreak()]}));
kids.push(h1("All 60 videos in detail"));
kids.push(para("Checked: each clip makes sense at that point in the story, doesn't give away the twist, and is filmed on the right login."));
P.videos.forEach(v=>{
  kids.push(h3(`${v.id}: ${v.hook}`));
  const who=w=>w=="me"?v.angry:v.other;
  const lines=a=>a.map(([w,x])=>`${who(w)}: ${x=="[PHOTO]"?"[photo: "+(v.photo||"")+"]":x}`).join("   •   ");
  kids.push(kv([
    ["Angry person",`${v.angry}. The DMs show the chat from ${v.angry}'s side, with “${v.dmname}” at the top.`],
    ["The fight (DMs)",lines(v.fight)],
    ["Film on",`${v.phone}'s login. Recording ${v.rec}, item ${v.idx}.`],
    ["Exactly what to film",v.step],
    ["Caption over your clip",v.overlay.join("  →  ")],
    ["Why this clip",v.why],
    ["The twist (DMs)",lines(v.twist)],
    ...(v.photo?[["Photo needed",v.photo]]:[]),
  ]));
  kids.push(para(""));
});

const doc=new Document({
  styles:{default:{document:{run:{font:FONT,size:21}}},
    paragraphStyles:[
      {id:"Title",name:"Title",basedOn:"Normal",run:{size:40,bold:true,color:"C2185B",font:FONT},paragraph:{spacing:{after:200}}},
      {id:"Heading1",name:"Heading 1",basedOn:"Normal",next:"Normal",quickFormat:true,run:{size:30,bold:true,color:"1D1520",font:FONT},paragraph:{outlineLevel:0}},
      {id:"Heading2",name:"Heading 2",basedOn:"Normal",next:"Normal",quickFormat:true,run:{size:25,bold:true,color:"C2185B",font:FONT},paragraph:{outlineLevel:1}},
      {id:"Heading3",name:"Heading 3",basedOn:"Normal",next:"Normal",quickFormat:true,run:{size:22,bold:true,color:"1D1520",font:FONT},paragraph:{outlineLevel:2}}]},
  numbering:{config:[{reference:"bul",levels:[{level:0,format:LevelFormat.BULLET,text:"•",alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:720,hanging:360}}}}]},
    ...numbered.map(r=>({reference:r,levels:[{level:0,format:LevelFormat.DECIMAL,text:"%1.",alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:720,hanging:360}}}}]}))]},
  sections:[{properties:{page:{size:{width:11906,height:16838},margin:{top:1440,right:1440,bottom:1440,left:1440}}},children:kids}]
});
Packer.toBuffer(doc).then(b=>{fs.writeFileSync('CoupleIn_filming_guide.docx',b);console.log('written',b.length)});

// Temporary script to generate 800 unique mailboxes
// Will be deleted after use

const fs = require('fs');

// ── Read existing usernames ──
const existingLines = fs.readFileSync('email boxes.txt', 'utf8').trim().split('\n');
const existingUsernames = new Set();
for (const line of existingLines) {
  const trimmed = line.trim();
  if (!trimmed) continue;
  const atIdx = trimmed.indexOf('@');
  if (atIdx > 0) {
    existingUsernames.add(trimmed.substring(0, atIdx).toLowerCase());
  }
}
console.log(`Existing usernames: ${existingUsernames.size}`);

// ── American first names (male + female) ──
const firstNamesMale = [
  'aaron','adam','adrian','aiden','alan','albert','alec','alex','alexander','alfie',
  'andrew','angel','anthony','antonio','archer','arthur','ashton','austin','avery','axel',
  'bailey','baron','barry','ben','benjamin','bennett','blake','bobbyj','brad','bradley',
  'brandon','brantley','braxton','brendan','brennan','brent','brett','brian','brody','brooks',
  'bruce','bryan','bryce','bryson','caleb','callum','cameron','carl','carlos','carson',
  'carter','casey','cedric','chad','chance','chandler','charles','charlie','chase','chris',
  'christian','christopher','clarence','clark','clay','clayton','clifford','clint','cody','cole',
  'colin','collin','colton','connor','cooper','corey','craig','cruz','curtis','cyrus',
  'dakota','dale','dallas','dalton','damian','damon','dan','dane','daniel','danny',
  'darren','darwin','davin','davis','dawson','dean','dennis','derek','deshawn','desmond',
  'devin','devon','diego','dillon','dominic','donald','donovan','dorian','doug','douglas',
  'drake','drew','dustin','dwight','dylan','easton','eddie','edgar','edmund','edward',
  'edwin','eli','elijah','elliot','ellis','emery','emmett','enrique','eric','ernest',
  'erwin','ethan','eugene','evan','everett','ezra','fabian','felix','fernando','finley',
  'finn','fletcher','flynn','ford','forrest','foster','francis','frank','franklin','fred',
  'frederick','gabriel','gage','garrett','gary','gavin','gene','george','gerald','giovanni',
  'glen','gordon','grady','graham','grant','grayson','gregory','griffin','grover','gunner',
  'gustavo','guy','hal','hank','hardy','harlan','harold','harris','harrison','harry',
  'harvey','hayden','heath','hector','henry','herman','holden','howard','hudson','hugh',
  'hugo','hunter','ian','irving','isaac','isaiah','ivan','jace','jack','jackson',
  'jacob','jaden','jake','jamal','james','jameson','jared','jarvis','jason','jasper',
  'javier','jayden','jaylen','jeff','jefferson','jeffrey','jennings','jeremy','jerome','jerry',
  'jesse','jimmy','joaquin','joe','joel','john','johnny','jonas','jonathan','jordan',
  'jorge','jose','joseph','joshua','josiah','juan','judd','julian','julius','justice',
  'justin','kai','kaleb','kane','karl','keaton','keegan','keith','kellan','kelvin',
  'kendall','kenneth','kent','kevin','kingsley','kirk','knox','kurt','kyle','lance',
  'landon','lane','larry','lawrence','lee','leo','leon','leonard','lester','levi',
  'lewis','liam','lincoln','lloyd','logan','lorenzo','louis','luca','lucas','luke',
  'luther','lyle','mack','malcolm','malik','marcus','mario','mark','marshall','martin',
  'marvin','mason','mateo','mathew','matt','matthew','maurice','maverick','max','maxwell',
  'melvin','micah','michael','miguel','miles','miller','milo','mitchell','mohammad','montgomery',
  'morgan','morris','moses','murphy','nash','nate','nathan','neal','nelson','nicholas',
  'noel','nolan','norman','oliver','omar','orlando','orson','oscar','otis','otto',
  'owen','pablo','parker','patrick','paul','paxton','pedro','percy','perry','pete',
  'peter','peyton','philip','phoenix','pierce','porter','preston','prince','quentin','quincy',
  'rafael','ralph','ramiro','ramon','randall','randy','raul','ray','raymond','reed',
  'reese','reggie','reid','remy','rene','rex','rhett','ricardo','richard','riley',
  'river','robert','robin','rocco','rodney','roger','roland','roman','ronald','rory',
  'ross','rowan','roy','ruben','russell','ryan','ryder','sam','samuel','santiago',
  'scott','sean','sebastian','sergio','seth','shane','shaun','sheldon','simon','skyler',
  'solomon','spencer','stanley','stefan','stephen','sterling','steve','steven','stewart','stone',
  'stuart','sullivan','tanner','taylor','terry','thaddeus','theo','theodore','thomas','tim',
  'timothy','tobias','todd','tony','trace','travis','trent','trevor','trey','tristan',
  'troy','tucker','turner','tyler','ulysses','vance','vaughn','vernon','victor','vince',
  'vincent','wade','walker','wallace','walter','ward','warren','wayne','wendell','wesley',
  'weston','will','william','willis','winston','wyatt','xavier','yuri','zachary','zander','zane'
];

const firstNamesFemale = [
  'abigail','addison','adriana','alexa','alexandra','alexis','alice','alina','allison','alyssa',
  'amanda','amber','amelia','andrea','angela','anna','annabelle','aria','ariana','ashley',
  'audrey','aurora','autumn','ava','avery','bailey','bella','bethany','bianca','blair',
  'briana','bridget','brittany','brooke','brooklyn','caitlin','cameron','camilla','candice','cara',
  'carmen','caroline','cassandra','catherine','celia','charlotte','chelsea','chloe','christina','claire',
  'clara','claudia','cora','courtney','crystal','daisy','dana','daniela','daphne','dawn',
  'deborah','destiny','diana','elena','elise','elizabeth','ella','ellie','emily','emma',
  'erica','erin','esther','eva','evelyn','faith','fiona','gabriella','gemma','genesis',
  'gianna','giselle','grace','hailey','hannah','harper','hazel','heather','helen','holly',
  'hope','ida','irene','iris','isabella','ivy','jacqueline','jade','jane','janet',
  'jasmine','jennifer','jessica','jillian','jocelyn','jordan','josephine','joyce','julia','juliana',
  'kaitlyn','karen','kate','katherine','kayla','kelly','kelsey','kendra','kimberly','kylie',
  'lacey','layla','leah','lena','leslie','lillian','lily','linda','lisa','lucia',
  'luna','lydia','mackenzie','madeline','madison','maggie','maia','mallory','margaret','maria',
  'mariana','martha','maya','megan','melanie','melissa','meredith','mia','michaela','michelle',
  'miranda','molly','monica','morgan','nadia','nancy','naomi','natalie','natasha','nicole',
  'nina','nora','olive','olivia','paige','paisley','pamela','patricia','paula','penelope',
  'peyton','phoebe','piper','quinn','rachel','raquel','reagan','rebecca','regina','renee',
  'riley','rosalie','rose','ruby','ruth','sabrina','sadie','samantha','sandra','sara',
  'sarah','savannah','scarlett','selena','serena','shelby','sierra','skylar','sofia','sophia',
  'stella','stephanie','summer','susan','sydney','talia','tamara','tara','tatiana','taylor',
  'tessa','tiffany','trinity','valentina','vanessa','veronica','victoria','violet','vivian','wendy',
  'willow','ximena','zara','zoe'
];

// ── Last names ──
const lastNames = [
  'adams','aguirre','allen','alvarez','anderson','andrews','armstrong','arnold','austin','avery',
  'bailey','baker','baldwin','banks','barker','barnes','barnett','barrett','barton','bass',
  'bates','beck','bell','bennett','benson','berry','bishop','black','blackwell','blair',
  'blake','blanchard','booth','bowen','boyd','bradshaw','brady','brewer','briggs','brooks',
  'brown','bryant','buchanan','burke','burnett','burns','burton','bush','butler','byrd',
  'caldwell','campbell','cannon','carey','carpenter','carr','carroll','carter','casey','castillo',
  'chambers','chandler','chang','chapman','chase','chen','clark','clarke','clay','clemons',
  'clements','cole','coleman','collins','combs','conway','cook','cooper','copeland','cortez',
  'cox','crane','crawford','cross','cunningham','curry','dalton','daniels','davidson','davis',
  'dawson','dean','decker','delgado','dennis','diaz','dickerson','dillon','dixon','doyle',
  'drake','dudley','duncan','dunn','duran','durham','eaton','edwards','elliott','ellis',
  'emerson','engel','erickson','espinoza','estrada','evans','farmer','fields','fisher','fitzgerald',
  'fleming','fletcher','flores','flynn','ford','foster','fowler','fox','francis','frank',
  'franklin','frazier','freeman','frost','fuller','gallagher','gallegos','garner','garrett','garrison',
  'gates','gibbs','gibson','gilbert','gill','glass','goldman','gomez','gonzalez','goodman',
  'gordon','grant','graves','gray','green','greene','griffin','grimes','guthrie','gutierrez',
  'hale','hall','hamilton','hammond','hampton','hansen','hardin','hardy','harmon','harper',
  'harris','harrison','hart','harvey','hawkins','hayden','hayes','haynes','heath','hensley',
  'henson','herman','hernandez','herrera','hicks','higgins','hill','hobbs','hodge','hoffman',
  'hogan','holland','holloway','holmes','holt','hood','hooper','horn','horton','houston',
  'howard','howell','hudson','huffman','hughes','hurst','ingram','irwin','jackson','jacobs',
  'james','jensen','johns','johnson','johnston','jones','jordan','joyce','kane','keller',
  'kelley','kelly','kemp','kendall','kennedy','kent','kerr','key','king','kirby',
  'kirkland','klein','knight','knox','lambert','lang','larsen','larson','lawrence','lawson',
  'leach','lester','levine','lewis','lindsey','little','livingston','lloyd','logan','long',
  'love','lowe','lucas','lynch','madden','malone','manning','marks','marsh','marshall',
  'martin','martinez','mason','mathews','maxwell','mayo','mcdonald','mcgee','mcguire','mckee',
  'mckenzie','mckinney','meadows','medina','mendez','mercer','meyer','miles','miller','mills',
  'mitchell','monroe','montgomery','moody','moore','morales','moran','morgan','morris','morrison',
  'morton','moss','mueller','mullen','munoz','murphy','murray','navarro','neal','nelson',
  'newman','newton','nichols','nolan','norris','norton','nunez','oconnor','oliver','olsen',
  'oneill','ortiz','osborne','owens','pace','padilla','page','palmer','park','parker',
  'parks','parsons','patel','patrick','patterson','patton','paul','payne','pearson','pena',
  'pence','perkins','perry','peters','phillips','pierce','pollard','pope','porter','powell',
  'powers','pratt','price','proctor','quinn','ramsey','randolph','ray','reed','reese',
  'reeves','reid','reynolds','rhodes','rice','richards','richardson','richmond','riley','rivers',
  'robbins','roberts','robertson','robinson','rodgers','rogers','roman','romero','roper','rose',
  'ross','rowe','ruiz','rush','russell','ryan','salazar','sanchez','sanders','santiago',
  'santos','saunders','savage','sawyer','schmidt','schneider','scott','sellers','shaw','shelton',
  'shepherd','shields','simmons','simon','simpson','sinclair','singh','slater','smith','snyder',
  'solomon','sosa','sparks','spears','stafford','stanley','stark','steele','stephens','stevens',
  'stevenson','stewart','stone','strong','sullivan','summers','sutton','swanson','tanner','tate',
  'taylor','terry','thomas','thompson','thornton','todd','torres','townsend','tran','travis',
  'tucker','turner','valdez','valentine','vargas','vasquez','vaughn','vega','villa','wade',
  'wagner','walker','wallace','walsh','walters','wang','ward','warner','warren','washington',
  'watkins','watson','watts','weaver','webb','weber','webster','weeks','welch','wells',
  'west','wheeler','whitaker','white','whitfield','whitney','wilkins','williams','williamson','willis',
  'wilson','winters','wise','wolfe','wood','woods','wright','wyatt','yang','york',
  'young','zamora','zimmerman'
];

const DOMAIN = 'newarento.ru';
const TARGET = 800;

// ── Password generator ──
function genPassword(len = 16) {
  const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz23456789';
  let pw = '';
  for (let i = 0; i < len; i++) {
    pw += chars[Math.floor(Math.random() * chars.length)];
  }
  return pw;
}

// ── Username generators ──
function randomFrom(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}
function randomNum(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

const generators = [
  // firstname.lastname
  () => {
    const fn = randomFrom([...firstNamesMale, ...firstNamesFemale]);
    const ln = randomFrom(lastNames);
    return `${fn}.${ln}`;
  },
  // firstnamelastname_initial  (e.g. anthonyw → anthonyw)
  () => {
    const fn = randomFrom([...firstNamesMale, ...firstNamesFemale]);
    const ln = randomFrom(lastNames);
    return `${fn}${ln[0]}`;
  },
  // initial.lastname
  () => {
    const fn = randomFrom([...firstNamesMale, ...firstNamesFemale]);
    const ln = randomFrom(lastNames);
    return `${fn[0]}.${ln}`;
  },
  // lastname+number
  () => {
    const ln = randomFrom(lastNames);
    return `${ln}${randomNum(1, 999)}`;
  },
  // firstname+number
  () => {
    const fn = randomFrom([...firstNamesMale, ...firstNamesFemale]);
    return `${fn}${randomNum(10, 999)}`;
  },
  // firstnameletter (e.g. deanb)
  () => {
    const fn = randomFrom([...firstNamesMale, ...firstNamesFemale]);
    const letter = 'abcdefghjklmnpqrstuvwxyz'[Math.floor(Math.random() * 24)];
    return `${fn}${letter}`;
  },
];

const allUsernames = new Set([...existingUsernames]);
const newEntries = [];

let attempts = 0;
while (newEntries.length < TARGET && attempts < 50000) {
  attempts++;
  const gen = generators[Math.floor(Math.random() * generators.length)];
  let username = gen().toLowerCase();
  
  // Sanitize: only alphanumeric, dots, hyphens
  username = username.replace(/[^a-z0-9.\-]/g, '');
  
  // Reject too short or too long
  if (username.length < 3 || username.length > 30) continue;
  
  // Check duplicate
  if (allUsernames.has(username)) continue;
  
  allUsernames.add(username);
  newEntries.push([username, genPassword()]);
}

console.log(`Generated: ${newEntries.length} (attempts: ${attempts})`);

// Sort by username
newEntries.sort((a, b) => a[0].localeCompare(b[0]));

// ── Write email list ──
const emailList = newEntries.map(e => `${e[0]}@${DOMAIN}`).join('\n') + '\n';
fs.writeFileSync('mailboxes_800.txt', emailList, 'utf8');
console.log(`Written mailboxes_800.txt (${newEntries.length} addresses)`);

// ── Write JS array for browser script ──
const jsArray = newEntries.map(e => `["${e[0]}","${e[1]}"]`).join(',\n');
fs.writeFileSync('_mailboxes_800_array.txt', jsArray, 'utf8');
console.log(`Written _mailboxes_800_array.txt`);

// ── Check for duplicates just in case ──
const uniqueCheck = new Set(newEntries.map(e => e[0]));
if (uniqueCheck.size !== newEntries.length) {
  console.error('WARNING: Internal duplicates found!');
} else {
  console.log('No duplicates found — all clean.');
}

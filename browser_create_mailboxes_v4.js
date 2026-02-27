// ============================================
// SCRIPT v4 — CREATE 200 MAILBOXES
// Paste in browser console (F12 → Console)
// while logged into ISPmanager
// ============================================

const mailboxes = [
["dave.holmes","3br8iLEooAfJBnxQ"],
["milesm","8Ezr8gJNXe9iWvzV"],
["gordon.reed","BbgTmgzXiUMqRbVz"],
["matt337","ZG7RjpsrnbAe8Hhu"],
["s.ross","jFsA4kWrga6WtJwo"],
["travisb","H7XhJgsGsi4AHZoG"],
["roland.maxwell","cFw8krqogCJunqAm"],
["francish","RuJLDhnHw6fbJPWb"],
["steved","MZs3mdSXPjgN7mxZ"],
["richardj","2Y7R4rbA9NypHarS"],
["lawrenceh","xGVtFyqrhYmYbH8t"],
["dave.perry","yJjLSjq5GMPBYAtd"],
["butler423","sMa4LVXwQJQhcy82"],
["eli.waters","jqCRNAvwwRDLnMpY"],
["r.moore","96u3o77GzzCBYycv"],
["darwins","vApyAPk8BCVHkr86"],
["codys","pUQ4674oNnjrgb2n"],
["richards889","mc9CdMZrk2B6FUHj"],
["m.matthews","BGAFTrmPGtdjmJ6k"],
["d.rose","ZrfKdWUoTuAQHqyd"],
["rodriguez245","mZ7r7hRpvKJvxAQb"],
["heathw","S9dBugLC4WFJyQFa"],
["aaron655","6fD2iTfshHxQyxVo"],
["hodge191","tMWBYakNZzQQGqzM"],
["j.dawson","JatvtxZkb4r2KRLt"],
["gene.garcia","biHzAQ2Qhh7iT7eb"],
["d.arnold","Cd9YiTHHe857hvAi"],
["baker865","PBRRcdUF5FQBsbX8"],
["brettg","P3gVRmjYWrW59JiL"],
["a.harrison","Ve9bNGrBNgFCgZL4"],
["willard983","E2o8pgKQ2iyWLVEt"],
["omars","nzTERpXPdwPjduwU"],
["todd.steele","VF7KJDRTZutrnhfA"],
["leonardr","FSzzGsm9uAoaLCQe"],
["trent156","aaD7uSfBc74X9Gsq"],
["haroldc","sxEvrLtRWEdkjTLv"],
["kendalld","fXmS6wGzbejySX2D"],
["king225","uabs69VSdvkWd3aJ"],
["patel985","SksMLguvsp223ahe"],
["rodney957","JYwN3wuYXqxf4NCi"],
["parker823","NzyXDt5dT6Wm2Lx4"],
["russell251","UDGbZV7nE8wyn8sj"],
["ivan.mccoy","GBrf3BmorpJucLzd"],
["dawsont","8SvQGVGx83soCpDm"],
["robertk","PHMGN75MtWV5irbJ"],
["jake747","ttenu8bgeFyNJUmY"],
["glen734","LhnKm8j6BPeabSev"],
["j.hunter","Q6XGWwhuxfmqpDbg"],
["dominicb","avXfNyBxMZPZu37a"],
["simon440","neMVZpxXE9K4payZ"],
["stanley.stephens","it9DCRoZwrCosKNp"],
["victor.reynolds","oxaM3MpVJtCgi7Nz"],
["evans170","dKyaEcUrsKUBgYKU"],
["curtis.peters","Zn6NF4juqNjGbvH8"],
["martin.lane","hZ37B9Haatu3szhS"],
["tylerc","2guQCMicSfGZ9VhG"],
["f.wells","BN83ja5UZh4MLZNg"],
["stuart.russell","ytt6Y4ACvgk22UNN"],
["g.vaughn","kPG2r5XB59tPpVgG"],
["wallace134","9SFGNPpc28kvmNKB"],
["shane.jenkins","abAECcz6fTnRFHVo"],
["jefferyc","mLNVJ7W7BJjNREfR"],
["c.martin","dEoTjsNpNWyzitZo"],
["j.hansen","ZGPe7u5eDmAZPQpe"],
["johnnyw","DB6Qijdjau2qPvZQ"],
["milesh","qxonidn6TS4owpFZ"],
["richardw","F44k4TM5UDXaKRbR"],
["j.freeman","VM5otAgfDbhEeVVY"],
["k.harvey","tBEiAz5RsFuGcHEh"],
["edwin590","TWNi4M8ToY3Dur7W"],
["fletcherk","WxSXHiCe6HMGm2VB"],
["kendalls","oXAkCCNYmULS2Ti2"],
["donovana","e9zGcjJqPLHYz83p"],
["m.hansen","ot5tqttZUXdaJAES"],
["h.simon","ya4m8nM6kT8CCE8V"],
["murray162","oRtXBKK8x4pEAy6m"],
["griffinc","fMwhfWtHDLN2HRNa"],
["oscar.peterson","TwKNGrDBcdJUAFnH"],
["stone229","bhbgvScPXVyoEpxH"],
["josephw","YKtrD4ZnuvhiifBc"],
["lyleh","rXpYNpNvokhNeFaT"],
["mariop","EnEERsPMphdmVnaQ"],
["anthony679","bZGKbmRcLhvZuTXq"],
["gibson522","8Lxnk8uzeY9iYbYP"],
["murrayu","DKMbgVmZcyT4SdqR"],
["i.jenkins","zcZq8Vimbt5iK3Wb"],
["griffin289","A8hsbu6pfHsyotCA"],
["murray263","8HkFgphb6buwXj3A"],
["t.lopez","MY3fBaD5qxuwJNts"],
["ryan206","Um5ten6KdAcFhfcz"],
["clarence525","Ku2LJNUSDZaNtuCz"],
["trent.mcgee","pe4ZYvXoDK4nxdeJ"],
["j.gross","SzAmfmzwmWLKDEBC"],
["jarvisr","cqVyqgJMLKpTdfLY"],
["lloyds","WMx9KA3ayQ5HL25r"],
["austin.watson","jeEHXU7cGE3Q3PH4"],
["s.parks","k7xgk6QbL2hWK3GL"],
["roman.garcia","HnNytDFac4d8dMTU"],
["charlesr","uLgTtjzRqWtcULVe"],
["long87","LN6NhG4diZhCZY7A"],
["j.kelly","o3VpmRZsuqHQoEQu"],
["nicholas.crane","LUqvGzPYk6PuLJms"],
["donovans","T6qpGVJj37jCqU8Z"],
["white232","XF2NwP66fbnDDq6F"],
["hank582","8qV3bAxHNTLuNLJn"],
["cameronn","3ZNdZTN9aXADdq6p"],
["larryr","L5qvrvy2Z3QSCSLX"],
["q.gray","5hwAxTnoHeRvbBd9"],
["walterm","vQA3Xgsf7UAAn6uY"],
["stanleyf","3KegYWhENpyTNnp7"],
["k.jordan","HueNpChLDzQMkSCS"],
["gilbert623","ePJNYFbVn79YvLQh"],
["ronald640","RjLf7LnbkDwN5Zj3"],
["ray709","BuxFzZqHcu55C744"],
["cameron232","s9KSJu4EAXwwigkw"],
["brooks116","uN8YJBk86qXqSJxB"],
["philipp","f6Uhn7FVvUFh8XJ3"],
["murray149","gj6Hj9gNGSRNfgHj"],
["liam869","cQXmyiYAhQSA6FZ6"],
["aland","nZ2nMd2cZpzshp4f"],
["jackson179","biNFZ9qRGqLixHFb"],
["d.kent","iFg9mRxKkbAyKra5"],
["chadd","vMVjCJLq5GR357jH"],
["m.wallace","BYBxfQgZb2wMBYYg"],
["kirkh","LyHzBcBhFBzRwa4S"],
["k.torres","QCwSJyF4pdfYMmqs"],
["reeset","9vLGJxKjaMHfsoqQ"],
["theodore982","a6hndzMWDfQhYg33"],
["chad342","9pFqP7VKvEwde4xd"],
["elijahh","iTWN46AqkuxL8Au9"],
["reedh","GgNcA9SMc6SYNPAM"],
["davis624","toQJp84xKT5LNwZw"],
["josephp","PjsxtAES7FWTWjVF"],
["glen.horton","VBeucsbgkrXdi3Y4"],
["jefferya","whTo7ZW9gA2YF8z4"],
["terrence258","fsuuAhBM28puECc5"],
["brandon.farmer","Cpt4NsArfS86tLUT"],
["carls","WYxihhmFsc6D2NAu"],
["zaner","Qb9Yw53c6RUT8hLz"],
["george.butler","mUAVipjngq2rU8Nf"],
["howards","aoofpXGs7wonio4H"],
["m.fletcher","YJmRVUez9UscoMse"],
["stephen209","7K6mZ2dRc2xcZi7y"],
["rossl","ukxGFMtaJYibL7cr"],
["elijahp","Z4QvxgwqmfP3ruCt"],
["anthony.mcgee","xHE2B33ZVeWZSVXP"],
["lester11","zjwh4562PhMbSkpz"],
["h.barnes","CEqKkxo7gBP5PmHL"],
["edwind","7G6akMAVhFFwtFyu"],
["crane196","SP7Xx9n7XjHbp7eP"],
["knox.larson","7TLgyJfvxq2eAN9N"],
["gabriel.morrison","KkzD888DgvATX9eK"],
["campbell561","osMXP7fgvprWey44"],
["fleming145","ze896EdewdGGRc3s"],
["lawrence30","22i2dNPxekemAzhi"],
["gordonp","j3aSsRTecFKu5zLp"],
["leonard.ward","5rZNam9ufr4T85SN"],
["curtis.taylor","ZitHL2CYiVXjHmmR"],
["l.gordon","aFtwMWhVLzmUDxze"],
["walter232","WFvYGqguFUmiu42K"],
["kirk780","DeZy6atVigpg2ezC"],
["derek368","PVo2ndyJEXGj56SS"],
["nolanw","F7umyEfqqCxzd8tf"],
["perrys","m3KSptHek6vRWnJq"],
["hamilton827","ugVighwDmKYa3RTa"],
["vernon.ellis","3ZA5u4VJnBQ5UhaL"],
["christianc","Kg6d2JfuXeBHukqR"],
["w.vaughn","zouFjbEQe32eP3DK"],
["walter573","tpH7DT3uSCzcS3Pm"],
["frank38","v4aB7aWQZHsUku2k"],
["nelson.hill","zhj7JAYvVnruwjUn"],
["james.farmer","9D6mDjkP2wbCF3Gu"],
["terrenced","yahNbBGn6Jyhz7Hx"],
["knoxk","NWyV88USUAYX2bDX"],
["clarencet","5T66peApJE7Da27E"],
["d.allen","jPpSWVfUFf6iCEQG"],
["douglasr","jQESjmW7X75EuWZR"],
["dean.paul","ijit4jNwB9ttUWrY"],
["kevinp","fE9YrXLHJuLWF3kH"],
["oscara","KGDYu7DLiRd7temJ"],
["j.ingram","ZDrJecYkVAHoJXib"],
["hunter650","2WkCZEwrStrRyvj2"],
["grahamw","VEURkHCBikcWaVEB"],
["carter740","GPFBAi2XnNqQAi5h"],
["clayton.brady","4wcogPFr544fGFn2"],
["c.white","pbQNoC5vuZ2ww9t3"],
["heathl","zW5Z75tGSjoqWjWX"],
["wendell807","TmtkAcEEgnMZwNGD"],
["greg744","56kkgHdmJjvPNQRo"],
["joelr","4xWzDFw4iLrCVB73"],
["roy.allen","d28t6727kP7tbKVY"],
["halc","QNTP5JsPHmQX4nuP"],
["knox.walsh","2CLHkokrp3aLLUss"],
["j.grimes","cSMrsUC2dfQ6o5qp"],
["albert.boone","GzTrcVGHecJ4Zut2"],
["h.edwards","tXQwhmG7VRvEroyV"],
["rexg","JDTkyXCkYJ4c5cXT"],
["frank.stephens","KfDYV2SFrPAGHH5M"],
["miller299","GNaRv2PzBBDh6RQu"],
["claytonp","tPrkExbuC9yhjMGD"]
];

const DOMAIN = "newarento.ru";
let created = 0, failed = 0, skipped = 0, errors = [];

async function createMailbox(name, password, index) {
  const total = mailboxes.length;
  const params = new URLSearchParams();
  params.append("out", "json");
  params.append("func", "email.edit");
  params.append("name", name);
  params.append("domain", DOMAIN);
  params.append("passwd", password);
  params.append("confirm", password);
  params.append("sok", "ok");

  try {
    const res = await fetch("/ispmgr?" + params.toString(), {
      method: "GET",
      credentials: "same-origin"
    });
    const text = await res.text();

    if (text.startsWith("<!") || text.startsWith("<html") || text.startsWith("<HTML")) {
      const res2 = await fetch("/ispmgr", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: params.toString(),
        credentials: "same-origin"
      });
      const text2 = await res2.text();
      if (text2.startsWith("<!") || text2.startsWith("<html")) {
        failed++;
        errors.push(name + ": HTML response (session expired?)");
        console.log("\u274c " + (index+1) + "/" + total + " FAIL: " + name + "@" + DOMAIN + " \u2014 HTML response");
        return;
      }
      handleResponse(text2, name, index);
    } else {
      handleResponse(text, name, index);
    }
  } catch(e) {
    failed++;
    errors.push(name + ": " + e.message);
    console.log("\u274c " + (index+1) + "/" + total + " ERROR: " + name + "@" + DOMAIN + " \u2014 " + e.message);
  }
}

function handleResponse(text, name, index) {
  const total = mailboxes.length;
  let data;
  try {
    data = JSON.parse(text);
  } catch(e) {
    failed++;
    errors.push(name + ": Invalid JSON: " + text.substring(0, 100));
    console.log("\u274c " + (index+1) + "/" + total + " FAIL: " + name + "@" + DOMAIN + " \u2014 bad JSON");
    return;
  }

  if (data.doc && data.doc.error) {
    const errMsg = JSON.stringify(data.doc.error);
    if (errMsg.includes("exist")) {
      skipped++;
      console.log("\u23ed\ufe0f " + (index+1) + "/" + total + " EXISTS: " + name + "@" + DOMAIN);
    } else {
      failed++;
      errors.push(name + ": " + errMsg);
      console.log("\u274c " + (index+1) + "/" + total + " FAIL: " + name + "@" + DOMAIN + " \u2014 " + errMsg);
    }
  } else {
    created++;
    console.log("\u2705 " + (index+1) + "/" + total + " OK: " + name + "@" + DOMAIN);
  }
}

(async () => {
  console.log("\ud83d\udd0d Testing API connection...");
  try {
    const test = await fetch("/ispmgr?out=json&func=email", { credentials: "same-origin" });
    const testText = await test.text();
    if (testText.startsWith("<!")) {
      console.error("\u274c Session expired! Refresh the page and try again.");
      return;
    }
    const testData = JSON.parse(testText);
    console.log("\u2705 API works! Current mailboxes in panel:", testData.doc?.elem?.length || "unknown");
  } catch(e) {
    console.error("\u274c API test failed:", e.message);
    return;
  }

  const total = mailboxes.length;
  console.log("\n\ud83d\ude80 Starting creation of " + total + " mailboxes for " + DOMAIN + "...\n");

  for (let i = 0; i < mailboxes.length; i++) {
    await createMailbox(mailboxes[i][0], mailboxes[i][1], i);
    await new Promise(r => setTimeout(r, 500));

    if ((i+1) % 50 === 0) {
      console.log("\n\ud83d\udcca Progress: " + (i+1) + "/" + total + " (OK: " + created + ", FAIL: " + failed + ", EXISTS: " + skipped + ")\n");
    }
  }

  console.log("\n============================");
  console.log("\u2705 Created:  " + created);
  console.log("\u23ed\ufe0f Existed:  " + skipped);
  console.log("\u274c Failed:   " + failed);
  console.log("============================");
  if (errors.length > 0) {
    console.log("\nErrors (first 20):");
    errors.slice(0, 20).forEach(function(e) { console.log("  " + e); });
  }
})();

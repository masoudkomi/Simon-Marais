"""Rebuild only this worker's deep-literature checkpoint records (no network)."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
STAMP = datetime.now(timezone.utc).isoformat()
CACHE = '.cache/literature/deep-literature-r1/'
records = {2020: [], 2021: [], 2025: []}

def source(year, key, url, cache, locator, status, scope):
    row = dict(key=key, url=url, locator=locator, status=status, read_scope=scope)
    if cache:
        p = ROOT / cache
        row.update(cache_path=cache, exists=p.exists())
        if p.exists():
            raw = p.read_bytes()
            row.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(), pdf_header=raw.startswith(b'%PDF'))
    records[year].append(row)

source(2020,'field-descent','https://personal.ntu.edu.sg/bernhard/Publications/pub/field.pdf',CACHE+'2020-leung-schmidt-field-descent.pdf','Definition2.6; TheoremA; Theorem4.3 p18','published; author version','Definitions, main theorem, application bound and surrounding proof read; p18 visually checked')
source(2020,'multiplier','https://personal.ntu.edu.sg/bernhard/Publications/pub/multipliers.pdf',CACHE+'2020-leung-ma-schmidt-multiplier.pdf','Theorem1.4 pp3–4; Corollary4.1; section5','published; author version','Main theorem and recursive hypotheses read, not a fresh full proof audit')
source(2020,'peluse','https://arxiv.org/abs/2003.04929v2',CACHE+'2020-peluse-asymptotic-v2.pdf','Theorem1.2; Theorem2.1; Lemma2.2 p3','published result; cached arXivv2','First four pages and residue proof read; p3 visually checked; asymptotic proof not independently reconstructed')
source(2020,'huang-schmidt','https://personal.ntu.edu.sg/bernhard/Publications/pub/Singer.pdf',CACHE+'2020-huang-schmidt-uniqueness.pdf','Section3 Results6–10; Lemmas12–15','published; author version','Definitions, scope and square-order reduction statements/proofs read through Lemma15')
source(2020,'abelian-n2','https://personal.ntu.edu.sg/bernhard/Publications/pub/blojunew.pdf',CACHE+'2020-blokhuis-jungnickel-schmidt-abelian-q2.pdf','Title and abstract p1','published; author version','Text extraction damaged; rendered p1 checked; no detailed theorem import')
source(2020,'gordon-small-lambda','https://arxiv.org/abs/2007.07292','.cache/literature/2020/initial-review-2/gordon-small-lambda-v1.pdf','arXiv Theorems5–6; published numbering differs','published; prior cached version','First four pages read, including exact collision criterion and contraction scope')
source(2020,'baumert-gordon','https://arxiv.org/abs/math/0304502',None,'Theorem5.1, cyclic planar section','published','Primary authored full-text passage found via indexed source; not newly cached')
source(2020,'alexeev-mixon','https://arxiv.org/abs/2510.19804v2','.cache/literature/2020/initial-review-2/alexeev-mixon-v2.pdf','Theorems8–9; section3','active preprint','First five pages read including direct proof and prime-order restriction; no proof-assistant artifact independently checked')
source(2020,'niu','https://arxiv.org/abs/2604.25214',None,'Abstract and bounded-search scope','active preprint; no theorem imported','Metadata/abstract only; complete proof expressly not supplied')
source(2020,'official','https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-solutions_1.pdf',None,'B4 heading and discussion p27','official competition source','Part(b) context and attribution only; no research on preliminary(a)')

source(2021,'bothmer','https://arxiv.org/abs/math/0605090v2','.cache/literature/2021/cited-24f2fc988b12860d.pdf','Theorem1.1 and characteristic-p transfer','published','All seven pages read; no novel proof claimed')
source(2021,'clo','https://arxiv.org/abs/1208.5404','.cache/literature/2021/cited-66c5af6a0f0239f5.pdf','Theorems3–5 pp4–5; paragraph3.6; Proposition19 pp15–16','published','Exact family/bad-prime/root hypotheses re-read; p15 rendered and visually checked')
source(2021,'draisma-dejong','https://ems.press/content/serial-issue-files/13698','.cache/literature/2021/draisma-de-jong-newsletter-2011-06-80.pdf','Proposition6 pp31–32; original Theorem7 p32–33','published, Theorem7 corrected by authors','Relevant original result and correction trail checked; no reliance on uncorrected family')
source(2021,'erratum','https://math-unibe.ch/jdraisma/publications/erratumcasasalvero.pdf',CACHE+'2021-draisma-dejong-erratum-2011.pdf','Entire one-page August2011 erratum','primary author correction','Entire text read')
source(2021,'massri','https://arxiv.org/abs/1806.09561v6','.cache/literature/2021/massri-1806.09561v6.pdf','Theorems7.9–7.10; Remark7.4','active v6 preprint, earlier withdrawals; no journal verified','Exact scope checked; complete author computation not newly audited')
source(2021,'massri-ssrn','https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4935880',None,'2024-08-24 author posting,14pp','author repository, not a journal acceptance','Metadata and matching restricted claim checked')
source(2021,'schaub-note','https://arxiv.org/abs/2312.08742v7',CACHE+'2021-schaub-spivakovsky-note-v7.pdf','Theorem5; added-in-press; Theorems9–10','active arXivv7','All five pages read; related2025 journal identity not publisher-fulltext verified')
source(2021,'schaub-description','https://arxiv.org/abs/2411.13967v1',CACHE+'2021-schaub-spivakovsky-description-v1.pdf','Theorem3.1; Corollary3.2; conditional characteristic-zero hypothesis','active preprint','All five pages read, including matrix construction and conditional bound')
source(2021,'schaub-published-bad-primes','https://doi.org/10.1007/s40687-024-00444-z',None,'Research in Mathematical Sciences11,31(2024)','publication verified on publisher page','Non-exhaustive list scope; not used as an exhaustive good-prime classification')
source(2021,'schaub-jca-record','https://doi.org/10.1216/jca.2025.17.199',None,'J.Commut.Algebra17(2),199–202(2025)','bibliographic record located; publisher inaccessible','Secondary records used only as metadata lead; exact correspondence to arXiv not asserted verified')
source(2021,'defrutos','https://uvadoc.uva.es/bitstream/handle/10324/3602/tesis367-130927.pdf?sequence=1',None,'2013 thesis introduction; Corollary2.3.4 printedp29','university dissertation; download timed out','Exact theorem and normalization read from indexed primary text; no full PDF/proof audit')
source(2021,'ghosh-universal','https://arxiv.org/abs/2501.09272v2','.cache/literature/2021/cited-40f9614065b33fc5.pdf','TheoremA; version/comment metadata','active major-revision preprint; no journal/withdrawal verified','Status and implication checked; no repeat full proof audit')
source(2021,'ghosh-finite','https://arxiv.org/abs/2402.18717v3','.cache/literature/2021/cited-78d1801ffc618164.pdf','Fixed-degree finiteness, not emptiness','AJM acceptance recorded in existing primary-source packet','Scope and author current-page statement checked')
source(2021,'ghosh-author','https://ghosh-soham.github.io/',None,'Publication list','primary author page','Finiteness acceptance distinguished from universal claim')
source(2021,'marashdeh','https://arxiv.org/abs/2608.14726v1','.cache/literature/2021/cited-f6c167df7cafd493.pdf','Introduction; support/scenario restrictions','active preprint','Introduction and relevance to support reductions; no theorem used as accepted axiom')
source(2021,'gasull','https://doi.org/10.1007/s44425-026-00047-6',None,'Section3.4, Proposition7, bibliography reference19','published survey, frontier statement conflicts with correction trail','Full relevant HTML section and cited reference checked; supplies no degree20 proof')
source(2021,'official','https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-solutions.pdf',None,'B4 heading; part(b) comments','official','Scope and attribution only; no preliminary(a) investigation')

source(2025,'official-setter','https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_solutions.pdf',CACHE+'2025-official-solutions-with-setter.pdf','B4 heading printedp16/25','official explicit proposer credit','Heading checked in text and rendering; only attribution/part(b) used')
source(2025,'mcnamara','https://petermc.net/maths/',None,'Peter J.McNamara identity and research list','primary author site','Representation-theory profile; no specific NL paper located')
source(2025,'chen-mihailescu','https://journal.hep.com.cn/caoms/EN/10.1007/s11401-026-0018-7','.cache/literature/2025/initial-review-1-chen-mihailescu-2026-complete.pdf','Equation1.3; Theorems1.1–1.3; footnote1 p390','published2026','Relevant exact theorem pages re-read and rendered; complete source previously reviewed in project')
source(2025,'dupuy','https://www.impan.pl/shop/en/publication/transaction/download/product/83678',CACHE+'2025-dupuy-2007.pdf','Theorem1.1 p392; following small-prime paragraph','published2007','First three pages read, exact integer/distinct-prime/e=1 hypotheses')
source(2025,'diagonal2008','https://doi.org/10.1007/978-3-211-74280-8_15',None,'Theorems1–4, version2.0 Sep17,2007; published2008','published chapter; author-uploaded text accessible','Author-posted complete text read in relevant sections; PDF download unsuccessful')
source(2025,'diagonal-author-text','https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren',None,'Primary content uploaded by PredaMihailescu','public author version','Theorem domains and first/second-case definitions checked; not a journal-proof audit')
source(2025,'bartolome-mihailescu','https://arxiv.org/abs/1412.5798v2',CACHE+'2025-bartolome-mihailescu-binary-thue-v2.pdf','Theorem1.2; Remark1.4; Theorem2.2','published IJNT2017; cached arXivv2 internal2021 date','First four pages read; repair appendix existence verified, computations not independently reconstructed')
source(2025,'hart-harvey-ong','https://arxiv.org/abs/1605.02398v1',CACHE+'2025-hart-harvey-ong-irregular-to-two-billion.pdf','Introduction tasks1–3; Table2','published Math.Comp.2017; finite computation','First four pages read; reported full range and class-group structure, not rerun')
source(2025,'strong-fc','https://arxiv.org/abs/2509.18275v1',CACHE+'2025-mihailescu-strong-fermat-catalan-v1.pdf','Equation2; Theorem1; Lemma5 pp8–9','active preprint; no journal acceptance verified','Entire ten pages read; p8 visually checked; concerns remain candidate and unaudited')
source(2025,'bennett-levin','https://secure.math.ubc.ca/~bennett/BeLe-Mona-2015.pdf','.cache/literature/2025/bennett-levin-2015.pdf','Proposition1; Theorem1','published2015','Existing exact signed-domain packet read before deeper search')
source(2025,'bugeaud-mihailescu','https://doi.org/10.7146/math.scand.a-15038','.cache/literature/2025/bugeaud-mihailescu-2007.pdf','Positive x,y domain; prime-term reductions','published2007; DOI matched existing primary reference','Existing source-domain distinction retained; no signed extension made')
source(2025,'chen-thesis','https://ediss.uni-goettingen.de/handle/11858/14935?locale-attribute=en&show=full',None,'2023 thesis metadata; PDF403','university repository, public metadata; PDF inaccessible','Metadata only; no full theorem/sign audit')
source(2025,'signed-survey','https://www.e-periodica.ch/cntmng?pid=ens-001%3A2002%3A48%3A%3A69',CACHE+'2025-bugeaud-survey-2002.pdf','Bugeaud–Mignotte2002 survey; section11 x<0','failed PDF retrieval: HTML response','Not treated as a read paper; response hash retained')
source(2025,'mihailescu2007','https://doi.org/10.1016/j.jnt.2006.10.010',None,'JNT124(2),380–395','published; original full text not obtained','q>(p−1)^2 known here only through exact2026 restatement; no original-theorem audit')

for year in records:
    source(year,'committee-current','https://www.simonmarais.org/aboutus.html',None,'Problem Committee2026','official current page','No historical backdating; /committees.html inaccessible')

logs = {
2020:[
 dict(utc_interval=['2026-10-16T17:02:49Z','2026-10-16T17:17:08Z'],activity='Read prior references/research/accepted partial notes; navigated Schmidt publication bibliography, Peluse, Gordon and Alexeev–Mixon; downloaded primary PDFs. Earlier exact per-call timestamps are not recoverable.',topics=['post-Gordon multiplier theorems','field descent','square descent','cyclic uniqueness versus existence','confirmed current committee names and attribution']),
 dict(utc_interval=['2026-10-16T17:17:08Z',STAMP],exact_queries=['"cyclic planar difference sets" "2025"','"cyclic projective planes" "2024" "prime power"','"cyclic" "prime power conjecture" square descent multiplier 2026','"Simon Marais" "taut" author'],activity='Followed primary author publication links to Huang–Schmidt and Blokhuis–Jungnickel–Schmidt; checked cited theorem hypotheses and rendered formulas; no computation launched')],
2021:[
 dict(utc_interval=['2026-10-16T17:02:49Z','2026-10-16T17:17:08Z'],activity='Read existing references/research/accepted normalization and partial packets; followed bibliographies to Schaub–Spivakovsky and deFrutos thesis; checked author homepages/status; cached two5-page preprints.',topics=['stronger rational-witness claims versus all-roots-rational','few-term prior results','bad-prime theorem hypotheses','universal proof status and separate finiteness acceptance']),
 dict(utc_interval=['2026-10-16T17:17:08Z',STAMP],exact_queries=['"Casas-Alvero" "rational" "20"','"Casas-Alvero" "rational roots" theorem','"Casas-Alvero" "rational" "witness"','"Casas-Alvero" "trinomials" Frutos','"Casas-Alvero" "rational coefficients" roots theorem','"Casas-Alvero" "rational numbers" shared roots','"Casas-Alvero" "rationnelles" racines','"Casas-Alvero" "racionales" testigos','"Casas-Alvero" "rational" "recycled"','"Casas-Alvero" "rational shared"','"Conjetura de Casas-Alvero" "monomios"','"Casas-Alvero" "20" "degree" rational solved','"Casas-Alvero" "degree 20" solved -site:scispace.com -site:proofatlas.ai -site:mathdb.com -site:wikipedia.org','"Casas-Alvero" "degree 24" Gasull','"Casas-Alvero" rational degree "20" "theorem" -site:scispace.com -site:researchgate.net -site:wikipedia.org -site:mathdb.com -site:proofatlas.ai','"Soham Ghosh" "Lemma 5.4" July 2026','"ON THE CASAS-ALVERO CONJECTURE" "10.1216/jca.2025.17.199"','"10.1216/jca.2025.17.199" Schaub Spivakovsky site:projecteuclid.org','site:uvadoc.uva.es "Corolario 2.3.4" "Casas"','site:uvadoc.uva.es/bitstream/10324/3602 "Teorema 2.3.1"','"Simon Marais" "Casas" "proposed"'],activity='Re-read exact CLO/Bothmer theorems; found original2011 author erratum; traced Gasull reference19; no primary July critique found/used; social/aggregator claims not mathematical evidence')],
2025:[
 dict(utc_interval=['2026-10-16T17:02:49Z','2026-10-16T17:17:08Z'],activity='Read prior references/research/accepted signed boundaries; located alternate official proposer credit; read entire strongFCpreprint, Chen theorem pages, diagonal author-posted text, and HHO introductory results.',topics=['signed Nagell–Ljunggren domains','class-number and prime-power nearby results','forward citations to diagonal criteria','Peter J.McNamara identity/publications']),
 dict(utc_interval=['2026-10-16T17:17:08Z',STAMP],exact_queries=['"Nagell-Ljunggren" "negative" 2026 2025','"Nagell-Ljunggren" "q > (p" Mihailescu 2007','Dupuy "Nagell" "2007" Acta Arithmetica class number','"Class Number Conditions" "Diagonal" Mihailescu pdf','Mihailescu "New bounds and conditions" Nagell Ljunggren pdf','"Cyclotomic Norm Diophantine" Chen 2025 theorem negative','"New bounds and conditions" "(p" "q"','"Nagell-Ljunggren" "negative" Bugeaud 2002 survey','"Peter McNamara" "Nagell"'],activity='Read original Dupuy theorem; checked Bartolome parameter condition and repair notice; rendered CMfootnote, strongFClemma, official setter heading; recorded thesis403 and invalid survey download')]
}

for year in records:
    folder = ROOT / f'problems/{year}-B4/notes'
    payload = dict(recorded_at_utc=STAMP, researcher='review_2021_j16_digits_r1 (new literature role)', requested_model='gpt-6.1-sol', requested_reasoning='max', effective_setting_readback='unavailable', scope=f'{year} B4(b) only', full_papers_tracked=False, sources=records[year])
    (folder/'deep-literature-r1-sources-v1.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    log = dict(recorded_at_utc=STAMP, timing_policy='UTC intervals bounded by clock/telemetry reads, not fabricated exact timestamps for each tool call. Earlier groups record topics/navigation when exact query text was not retained.', prior_inputs=[str((ROOT/f'problems/{year}-B4'/x).relative_to(ROOT)) for x in ['references.md','research.md']], entries=logs[year], access_failures={'2020':['No explicit B4individual proposer credit found','/committees.html inaccessible'],'2021':['UVAthesis HTTPconnection timeout repeated incloneescalated retry','JCA DOI/ProjectEuclid inaccessible','Secondary Julycritique lead had no verified primary mathematical source'],'2025':['Göttingen thesisPDF403, not bypassed','2008chapter CiteSeerPDF404; authorpostedtext accessible','EPeriodica HTTPsuccess returned HTML, invalid asPDF','Original2007bound fulltext not obtained']}[str(year)], computation_policy='Only PDF extraction/rendering, hashes and record construction; no CAS or mathematical exhaustive search launched.', telemetry=dict(observed_total_weekly_used_percent=14,reset_unix=1792745187,observed_during='checkpoint finalization; exact per-call wall-clock not logged',cutoff_percent=90))
    log['commands_and_dependencies'] = {
        'rebuild': '.venv/bin/python problems/2021-B4/notes/deep-literature-r1-build-records-v1.py',
        'download_template': "curl -L --fail --silent --show-error --max-time 30 '<source_url>' -o '<cache_path>'",
        'pdf_read': 'Python3.12.14, pypdf.PdfReader; extract_text on the exact page ranges recorded per source',
        'pdf_render_template': 'pdftoppm -f PAGE -l PAGE -scale-to 1600 -png -singlefile SOURCE_PDF CACHE_PREFIX',
        'render_inspection': 'view_image; theorem/footnote pages recorded in source read_scope; official2025 heading only used',
        'cache_ignore_check': 'git check-ignore .cache/literature/deep-literature-r1/<downloaded-file>; representative files confirmed ignored',
        'verification': 'Recomputed SHA256 for every cached source entry and every tracked checkpoint artifact; no missing cached entries; invalid survey HTML separately marked pdf_header=false',
        'native_CAS_jobs': [],
    }
    (folder/'deep-literature-r1-search-log-v1.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
    artifacts = []
    for p in sorted(folder.glob('deep-literature-r1-*')):
        if p.name.endswith('manifest-v1.json'):
            continue
        raw=p.read_bytes()
        artifacts.append(dict(path=str(p.relative_to(ROOT)),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()))
    manifest = dict(recorded_at_utc=STAMP,status='literature checkpoint, no proof promotion',artifacts=artifacts)
    target=folder/'deep-literature-r1-manifest-v1.json'
    target.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(year,len(records[year]),'sources',len(artifacts),'artifacts',hashlib.sha256(target.read_bytes()).hexdigest(),flush=True)

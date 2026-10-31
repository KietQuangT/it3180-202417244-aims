# B├ío c├ío thß║úo luß║¡n Lab 04: Release Flow & Phi├¬n bß║ún ph├ít h├ánh

## 1. C├óu hß╗Åi nhanh (Slide 47)
### C├óu hß╗Åi: V├¼ sao chuß║⌐n bß╗ï tr├¬n `master` tr╞░ß╗¢c, kh├┤ng sß╗¡a tr├¬n nh├ính release?
**Trß║ú lß╗¥i:**
- **Nguy├¬n tß║»c cß╗æt l├╡i cß╗ºa Release Flow:** Nh├ính `release/*` chß╗ë l├á nh├ính ph├íi sinh phß╗Ñc vß╗Ñ ph├ít h├ánh v├á ─æ├│ng b─âng baseline, **tuyß╗çt ─æß╗æi kh├┤ng bao giß╗¥ merge ng╞░ß╗úc lß║íi v├áo nh├ính `master`**.
- Do ─æ├│, mß╗ìi c├┤ng viß╗çc chuß║⌐n bß╗ï cho phi├¬n bß║ún ph├ít h├ánh nh╞░: cß║¡p nhß║¡t sß╗æ phi├¬n bß║ún (`__version__`), chß╗ënh sß╗¡a `CHANGELOG.md`, kiß╗âm tra t├¡nh ß╗òn ─æß╗ïnh m├ú nguß╗ôn ─æß╗üu phß║úi ─æ╞░ß╗úc thß╗▒c hiß╗çn ho├án chß╗ënh tr├¬n nh├ính `master` tr╞░ß╗¢c (th├┤ng qua nh├ính chuß║⌐n bß╗ï `topic/prepare-release-x.x.x` v├á PR).
- Khi `master` ─æ├ú ß╗ƒ trß║íng th├íi ho├án hß║úo nhß║Ñt, ta mß╗¢i rß║╜ nh├ính `release/labXX` tß╗½ commit ─æ├│. Nß║┐u sß╗¡a trß╗▒c tiß║┐p tr├¬n `release/*`, c├íc thay ─æß╗òi vß╗ü phi├¬n bß║ún v├á t├ái liß╗çu sß║╜ bß╗ï kß║╣t lß║íi tr├¬n nh├ính release v├á kh├┤ng bao giß╗¥ tß╗▒ ─æß╗Öng c├│ mß║╖t tr├¬n `master`, dß║½n ─æß║┐n sai lß╗çch cß║Ñu h├¼nh trong c├íc phi├¬n bß║ún t╞░╞íng lai.

---

## 2. C├óu hß╗Åi thß║úo luß║¡n (Slide 52)
### C├óu hß╗Åi 1: V├¼ sao `release/*` kh├┤ng merge v├áo master? So s├ính vß╗¢i GitFlow.
**Trß║ú lß╗¥i:**
- **Trong Release Flow:**
  - Nh├ính `master` lu├┤n lu├┤n ─æi thß║│ng vß╗ü ph├¡a tr╞░ß╗¢c theo d├▓ng chß║úy li├¬n tß╗Ñc (continuous delivery mindset). Nh├ính `release/*` chß╗ë rß║╜ nh├ính ─æß╗â l├ám nhiß╗çm vß╗Ñ ─æ├│ng b─âng v├á bß║úo tr├¼ phi├¬n bß║ún (maintenance line).
  - Kh├┤ng merge `release/*` ng╞░ß╗úc lß║íi v├áo `master` gi├║p nh├ính ch├¡nh kh├┤ng bß╗ï ├┤ nhiß╗àm bß╗ƒi c├íc commit trung gian, tr├ính tß║ío ra c├íc merge commit lß╗Ön xß╗Ön hoß║╖c v├┤ t├¼nh ghi ─æ├¿ c├íc t├¡nh n─âng mß╗¢i ─æang ph├ít triß╗ân tr├¬n `master`. Khi cß║ºn ─æ╞░a bß║ún sß╗¡a lß╗ùi tß╗½ release vß╗ü master, ta sß╗¡ dß╗Ñng c├┤ng cß╗Ñ `cherry-pick -x` ─æß╗â nhß║╖t ch├¡nh x├íc tß╗½ng commit sß╗¡a lß╗ùi cß╗Ñ thß╗â.
- **So s├ính vß╗¢i GitFlow:**
  - GitFlow duy tr├¼ ─æß╗ông thß╗¥i 2 nh├ính v─⌐nh viß╗àn: `main` (sß║ún xuß║Ñt) v├á `develop` (ph├ít triß╗ân t├¡ch hß╗úp). Nh├ính `release` ─æ╞░ß╗úc tß║ío tß╗½ `develop`, v├á khi ho├án tß║Ñt phß║úi merge v├áo **cß║ú** `main` lß║½n `develop`.
  - Hß║ín chß║┐ cß╗ºa GitFlow: Cß║Ñu tr├║c merge 2 chiß╗üu rß║Ñt phß╗⌐c tß║íp, dß╗à g├óy ra t├¼nh trß║íng xung ─æß╗Öt k├⌐p (merge hell), kh├│ quß║ún l├╜ khi c├│ nhiß╗üu phi├¬n bß║ún c├╣ng chß║íy ─æß╗ông thß╗¥i v├á l├ám chß║¡m chu kß╗│ ph├ít h├ánh nhanh hiß╗çn ─æß║íi.

### C├óu hß╗Åi 2: V├¼ sao l├¬n `1.0.0` m├á kh├┤ng phß║úi `0.4.0`?
**Trß║ú lß╗¥i:**
- **Quy tß║»c Semantic Versioning (SemVer):**
  - ─Éß╗ïnh dß║íng phi├¬n bß║ún: `MAJOR.MINOR.PATCH`.
  - C├íc phi├¬n bß║ún `0.y.z` ─æß║íi diß╗çn cho giai ─æoß║ín ph├ít triß╗ân ban ─æß║ºu (Initial Development Phase), khi phß║ºn mß╗üm ch╞░a ho├án thiß╗çn, API c├│ thß╗â thay ─æß╗òi bß║Ñt kß╗│ l├║c n├áo v├á ch╞░a c├│ cam kß║┐t ß╗òn ─æß╗ïnh.
  - Phi├¬n bß║ún `1.0.0` ─æ├ính dß║Ñu cß╗Öt mß╗æc quan trß╗ìng: **Sß║ún phß║⌐m ch├¡nh thß╗⌐c ─æß║ít trß║íng th├íi ho├án thiß╗çn ─æß║ºu ti├¬n (First Public/Production Release)**. Tß║íi thß╗¥i ─æiß╗âm Lab 04, dß╗▒ ├ín `AIMS-mini` ─æ├ú c├│ cß║Ñu tr├║c package chuß║⌐n mß╗▒c, c├íc t├¡nh n─âng cß╗æt l├╡i (Cart, DVD, t├¼m kiß║┐m, giß║úm gi├í, in h├│a ─æ╞ín), bß╗Ö unit test ─æß║ºy ─æß╗º v├á t├ái liß╗çu ca sß╗¡ dß╗Ñng.
  - Viß╗çc gß║»n sß╗æ `1.0.0` x├íc lß║¡p mß╗Öt baseline ch├¡nh thß╗⌐c, ─æ╞░a ra cam kß║┐t vß╗ü t├¡nh ß╗òn ─æß╗ïnh v├á t╞░╞íng th├¡ch cho ng╞░ß╗¥i sß╗¡ dß╗Ñng thay v├¼ coi n├│ chß╗ë l├á bß║ún thß╗¡ nghiß╗çm `0.4.0`.

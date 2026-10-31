# B├ío c├ío thß║úo luß║¡n Lab 02: Feature/Topic Flow & Pull Request

## C├óu hß╗Åi thß║úo luß║¡n (Slide 35)

### C├óu hß╗Åi 1: V├¼ sao phß║úi ─æß╗ông bß╗Ö master tr╞░ß╗¢c khi PR?
**Trß║ú lß╗¥i:**
- **Nguy├¬n l├╜ Shift Left & Giß║úm xung ─æß╗Öt:** Trong m├┤i tr╞░ß╗¥ng l├ám viß╗çc song song nhiß╗üu nh├ính/nhiß╗üu lß║¡p tr├¼nh vi├¬n, nh├ính `master` li├¬n tß╗Ñc tiß║┐n l├¬n ph├¡a tr╞░ß╗¢c do c├íc PR kh├íc ─æ╞░ß╗úc merge v├áo.
- Khi nh├ính t├¡nh n─âng ─æ╞░ß╗úc ─æß╗ông bß╗Ö vß╗¢i `master` (th├┤ng qua `git fetch origin` v├á `git merge origin/master`), lß║¡p tr├¼nh vi├¬n c├│ thß╗â ph├ít hiß╗çn v├á xß╗¡ l├╜ mß╗ìi xung ─æß╗Öt ph├ít sinh ngay tß║íi m├íy c├í nh├ón (local environment), thay v├¼ ─æß║⌐y xung ─æß╗Öt l├¬n GitHub.
- **─Éß║úm bß║úo t├¡nh t╞░╞íng th├¡ch t├¡ch hß╗úp:** Gi├║p lß║¡p tr├¼nh vi├¬n chß║íy thß╗¡ nghiß╗çm kiß╗âm thß╗¡ (`main.py`, unit test) tr├¬n m├ú nguß╗ôn ─æ├ú t├¡ch hß╗úp ─æß╗â x├íc nhß║¡n rß║▒ng t├¡nh n─âng mß╗¢i hoß║ít ─æß╗Öng h├ái h├▓a vß╗¢i nhß╗»ng thay ─æß╗òi mß╗¢i nhß║Ñt cß╗ºa hß╗ç thß╗æng tr╞░ß╗¢c khi gß╗¡i PR cho CCB/Reviewer ph├¬ duyß╗çt.

---

### C├óu hß╗Åi 2: Khi n├áo kh├┤ng ─æ╞░ß╗úc rebase?
**Trß║ú lß╗¥i:**
- **Quy tß║»c v├áng cß╗ºa Git Rebase:** Kh├┤ng bao giß╗¥ thß╗▒c hiß╗çn rebase tr├¬n c├íc nh├ính c├┤ng khai/─æ├ú ─æ╞░ß╗úc chia sß║╗ (public/shared branches) nh╞░ `master`, `main`, `release/*` hoß║╖c nh├ính ─æang c├│ nhiß╗üu ng╞░ß╗¥i c├╣ng l├ám viß╗çc chung.
- **L├╜ do:** Lß╗çnh rebase sß║╜ viß║┐t lß║íi to├án bß╗Ö lß╗ïch sß╗¡ commit (tß║ío ra c├íc commit hash/SHA mß╗¢i thay thß║┐ commit c┼⌐). Khi ng╞░ß╗¥i kh├íc pull vß╗ü, c├óy lß╗ïch sß╗¡ Git cß╗Ñc bß╗Ö cß╗ºa hß╗ì sß║╜ bß╗ï rß║╜ nh├ính xung ─æß╗Öt nghi├¬m trß╗ìng vß╗¢i remote, dß║½n ─æß║┐n thß║úm hß╗ìa hß╗úp nhß║Ñt (merge hell) v├á mß║Ñt dß║Ñu vß║┐t lß╗ïch sß╗¡.
- **Chß╗ë sß╗¡ dß╗Ñng rebase khi:** L├ám viß╗çc tr├¬n nh├ính ri├¬ng t╞░ cß╗ºa bß║ún th├ón (local feature branch) ch╞░a tß╗½ng push l├¬n remote, hoß║╖c nh├ính chß╗ë mß╗Öt m├¼nh m├¼nh kiß╗âm so├ít nhß║▒m mß╗Ñc ─æ├¡ch l├ám gß╗ìn g├áng lß╗ïch sß╗¡ commit tr╞░ß╗¢c khi tß║ío PR.

---

### C├óu hß╗Åi 3: `feature/*` kh├íc `topic/*` ra sao?
**Trß║ú lß╗¥i:**
- **Nh├ính `feature/*` (Feature branch):**
  - D├╣ng ─æß╗â ph├ít triß╗ân c├íc t├¡nh n─âng nghiß╗çp vß╗Ñ cß╗Ñ thß╗â cß╗ºa sß║ún phß║⌐m phß║ºn mß╗üm (v├¡ dß╗Ñ: `feature/cart-print`, `feature/discount`, `feature/search-by-title`).
  - Trß╗▒c tiß║┐p sß╗¡a ─æß╗òi hoß║╖c mß╗ƒ rß╗Öng logic nghiß╗çp vß╗Ñ trong m├ú nguß╗ôn ß╗⌐ng dß╗Ñng (`aims/cart.py`, `aims/search.py`).
  - Th╞░ß╗¥ng c├│ v├▓ng ─æß╗¥i theo tiß║┐n ─æß╗Ö cß╗ºa t├¡nh n─âng v├á ─æi k├¿m c├íc b├ái kiß╗âm thß╗¡ chß╗⌐c n─âng (functional tests).
- **Nh├ính `topic/*` (Topic branch):**
  - D├╣ng cho c├íc chß╗º ─æß╗ü ngß║»n hß║ín, c├┤ng viß╗çc hß╗ù trß╗ú kß╗╣ thuß║¡t hoß║╖c t├ái liß╗çu phi chß╗⌐c n─âng (v├¡ dß╗Ñ: `topic/pr-template`, `topic/use-case-diagram`, `topic/prepare-release-1.0.0`).
  - Phß║ím vi thay ─æß╗òi th╞░ß╗¥ng tß║¡p trung v├áo cß║Ñu h├¼nh dß╗▒ ├ín, quy tr├¼nh (`.github/`), t├ái liß╗çu kß╗╣ thuß║¡t (`docs/`) hoß║╖c chuß║⌐n bß╗ï phi├¬n bß║ún ph├ít h├ánh (`CHANGELOG.md`).

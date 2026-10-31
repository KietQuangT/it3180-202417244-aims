# B├ío c├ío thß║úo luß║¡n Lab 01: Thiß║┐t lß║¡p m├┤i tr╞░ß╗¥ng & Refactor Flow

## 1. C├óu hß╗Åi nhanh (Slide 19)
### C├óu hß╗Åi: Cß║Ñu h├¼nh `--global` ─æ╞░ß╗úc l╞░u ß╗ƒ ─æ├óu? Kh├íc g├¼ so vß╗¢i `--local`?
**Trß║ú lß╗¥i:**
- **N╞íi l╞░u trß╗»:**
  - Cß║Ñu h├¼nh `--global` ─æ╞░ß╗úc l╞░u trong tß╗çp `.gitconfig` tß║íi th╞░ mß╗Ñc ng╞░ß╗¥i d├╣ng (`~/.gitconfig` tr├¬n Linux/macOS hoß║╖c `C:\Users\<Username>\.gitconfig` tr├¬n Windows).
  - Cß║Ñu h├¼nh `--local` ─æ╞░ß╗úc l╞░u trong tß╗çp `.git/config` ngay tß║íi th╞░ mß╗Ñc gß╗æc cß╗ºa repository ─æang l├ám viß╗çc.
- **Sß╗▒ kh├íc biß╗çt:**
  - Phß║ím vi ß║únh h╞░ß╗ƒng: `--global` ├íp dß╗Ñng cho to├án bß╗Ö c├íc repository tr├¬n m├íy t├¡nh ─æß╗æi vß╗¢i user hiß╗çn tß║íi; `--local` chß╗ë ├íp dß╗Ñng ri├¬ng cho ch├¡nh repository ─æ├│.
  - Mß╗⌐c ─æß╗Ö ╞░u ti├¬n: Cß║Ñu h├¼nh `--local` c├│ ─æß╗Ö ╞░u ti├¬n cao h╞ín v├á sß║╜ ghi ─æ├¿ l├¬n cß║Ñu h├¼nh `--global` nß║┐u c├│ xung ─æß╗Öt cß║Ñu h├¼nh (v├¡ dß╗Ñ: d├╣ng email c├┤ng viß╗çc cho mß╗Öt repo cß╗Ñ thß╗â thay v├¼ email c├í nh├ón chung).

---

## 2. C├óu hß╗Åi thß║úo luß║¡n (Slide 26)
### C├óu hß╗Åi 1: V├¼ sao d├╣ng `git mv`?
**Trß║ú lß╗¥i:**
- Lß╗çnh `git mv` vß╗½a di chuyß╗ân/─æß╗òi t├¬n file trong working directory, vß╗½a tß╗▒ ─æß╗Öng cß║¡p nhß║¡t v├á ghi nhß║¡n h├ánh vi ─æß╗òi t├¬n v├áo staging area (`index`).
- Gi├║p Git giß╗» ─æ╞░ß╗úc t├¡nh li├¬n tß╗Ñc cß╗ºa lß╗ïch sß╗¡ quß║ún l├╜ phi├¬n bß║ún (bß║úo to├án commit history). Nhß╗¥ ─æ├│, ta c├│ thß╗â truy vß║┐t lß╗ïch sß╗¡ c├íc phi├¬n bß║ún c┼⌐ cß╗ºa tß╗çp sau khi ─æß╗òi t├¬n bß║▒ng lß╗çnh `git log --follow <─æ╞░ß╗¥ng_dß║½n_mß╗¢i>`.
- Nß║┐u chß╗ë d├╣ng lß╗çnh `mv` hoß║╖c di chuyß╗ân file thß╗º c├┤ng bß║▒ng hß╗ç ─æiß╗üu h├ánh, Git ban ─æß║ºu sß║╜ xem ─æ├│ l├á h├ánh ─æß╗Öng x├│a tß╗çp c┼⌐ (deleted) v├á tß║ío tß╗çp mß╗¢i ho├án to├án (untracked), dß╗à dß║½n ─æß║┐n sai s├│t khi stage v├á mß║Ñt t├¡nh trß╗▒c quan trong lß╗ïch sß╗¡ thay ─æß╗òi.

### C├óu hß╗Åi 2: `release/lab01` c├│ phß║úi baseline kh├┤ng?
**Trß║ú lß╗¥i:**
- **C├│.** Trong Quß║ún l├╜ cß║Ñu h├¼nh phß║ºn mß╗üm (SCM), Baseline l├á mß╗Öt cß║Ñu h├¼nh mß╗æc chuß║⌐n ─æ├ú ─æ╞░ß╗úc kiß╗âm thß╗¡, nghiß╗çm thu v├á thß╗æng nhß║Ñt tß║íi mß╗Öt thß╗¥i ─æiß╗âm x├íc ─æß╗ïnh.
- Nh├ính `release/lab01` ─æ├ính dß║Ñu trß║íng th├íi ß╗òn ─æß╗ïnh ─æß║ºu ti├¬n cß╗ºa m├ú nguß╗ôn sau khi ─æ├ú ho├án th├ánh t├íi cß║Ñu tr├║c (refactor package `aims/`, kiß╗âm tra chß║íy `python main.py` ra ─æ├║ng kß║┐t quß║ú `63.89 $`).
- Baseline n├áy ─æ╞░ß╗úc "─æ├│ng b─âng" ─æß╗â nß╗Öp b├ái v├á l├ám c╞í sß╗ƒ ─æß╗æi chuß║⌐n cho c├íc giai ─æoß║ín ph├ít triß╗ân tiß║┐p theo; kh├┤ng ─æ╞░ß╗úc ph├⌐p sß╗¡a ─æß╗òi t├╣y tiß╗çn m├á chß╗ë ─æ╞░ß╗úc cß║¡p nhß║¡t qua quy tr├¼nh kiß╗âm so├ít thay ─æß╗òi chß║╖t chß║╜.

### C├óu hß╗Åi 3: V├¼ sao kh├┤ng commit thß║│ng master d├╣ l├ám mß╗Öt m├¼nh?
**Trß║ú lß╗¥i:**
- **Tu├ón thß╗º nguy├¬n tß║»c SCM (Change Control):** Viß╗çc kh├┤ng commit trß╗▒c tiß║┐p l├¬n `master` gi├║p h├¼nh th├ánh kß╗╖ luß║¡t quy tr├¼nh l├ám viß╗çc chuß║⌐n nghiß╗çp nghiß╗çp. Mß╗ìi thay ─æß╗òi ─æß╗üu phß║úi ─æ╞░ß╗úc c├┤ lß║¡p tr├¬n mß╗Öt nh├ính ri├¬ng (feature/refactor branch).
- **Kiß╗âm so├ít rß╗ºi ro v├á tß╗▒ review (Self-Review):** Khi tß║ío Pull Request, lß║¡p tr├¼nh vi├¬n c├│ c╞í hß╗Öi nh├¼n lß║íi to├án bß╗Ö diff (`Files changed`) ─æß╗â r├á so├ít lß╗ùi c├║ ph├íp, tß╗çp thß╗½a (nh╞░ `__pycache__`) tr╞░ß╗¢c khi hß╗úp nhß║Ñt.
- **T├¡ch hß╗úp tß╗▒ ─æß╗Öng v├á khß║ú n─âng mß╗ƒ rß╗Öng:** Nh├ính `master` lu├┤n lu├┤n ß╗ƒ trß║íng th├íi "Deployable" (c├│ thß╗â ph├ít h├ánh/chß║íy ─æ╞░ß╗úc). Nß║┐u sau n├áy c├│ cß╗Öng sß╗▒ hoß║╖c t├¡ch hß╗úp hß╗ç thß╗æng kiß╗âm thß╗¡ CI/CD, quy tr├¼nh PR sß║╜ bß║úo vß╗ç nh├ính ch├¡nh kh├┤ng bao giß╗¥ bß╗ï ph├í vß╗í.

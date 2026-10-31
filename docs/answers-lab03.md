# B├ío c├ío thß║úo luß║¡n Lab 03: Bugfix Flow, Xung ─æß╗Öt & Ho├án t├íc

## C├óu hß╗Åi thß║úo luß║¡n (Slide 43)

### C├óu hß╗Åi 1: Merge base l├á g├¼?
**Trß║ú lß╗¥i:**
- **─Éß╗ïnh ngh─⌐a:** Merge base giß╗»a hai nh├ính (hoß║╖c hai commit cß╗Ñ thß╗â A v├á B) l├á commit tß╗ò ti├¬n chung gß║ºn nhß║Ñt (best common ancestor) cß╗ºa cß║ú hai nh├ính ─æ├│ trong ─æß╗ô thß╗ï c├│ h╞░ß╗¢ng kh├┤ng chu tr├¼nh (DAG) cß╗ºa Git.
- **Vai tr├▓ trong qu├í tr├¼nh hß╗úp nhß║Ñt (3-way merge):**
  - Khi thß╗▒c hiß╗çn lß╗çnh merge hoß║╖c giß║úi quyß║┐t xung ─æß╗Öt, Git kh├┤ng chß╗ë so s├ính trß╗▒c tiß║┐p nh├ính A vß╗¢i nh├ính B m├á d├╣ng thuß║¡t to├ín 3 chiß╗üu (3-way merge) dß╗▒a tr├¬n 3 ─æiß╗âm:
    1. Trß║íng th├íi tß║íi `merge base` (gß╗æc chung ban ─æß║ºu).
    2. Trß║íng th├íi tß║íi ─æß║ºu nh├ính A (nh├ính ─æ├¡ch).
    3. Trß║íng th├íi tß║íi ─æß║ºu nh├ính B (nh├ính nguß╗ôn).
  - Bß║▒ng c├ích so s├ính xem tß╗çp tin ─æ├ú thay ─æß╗òi nh╞░ thß║┐ n├áo tß╗½ `merge base` tß╗¢i tß╗½ng nh├ính, Git c├│ thß╗â tß╗▒ ─æß╗Öng t├¡ch hß╗úp c├íc thay ─æß╗òi kh├┤ng tr├╣ng d├▓ng v├á chß╗ë gß║»n cß╗¥ xung ─æß╗Öt (conflict markers `<<<<<<<`, `=======`, `>>>>>>>`) khi cß║ú hai nh├ính c├╣ng sß╗¡a ─æß╗òi c├╣ng mß╗Öt v├╣ng d├▓ng m├ú so vß╗¢i gß╗æc chung `merge base`.
- C├│ thß╗â t├¼m SHA cß╗ºa merge base bß║▒ng lß╗çnh: `git merge-base branchA branchB`.

---

### C├óu hß╗Åi 2: V├¼ sao `master` / `release/*` phß║úi d├╣ng `revert` thay v├¼ `reset`?
**Trß║ú lß╗¥i:**
- **C╞í chß║┐ hoß║ít ─æß╗Öng:**
  - `git reset` (nhß║Ñt l├á `--hard`) dß╗ïch chuyß╗ân con trß╗Å nh├ính l├╣i vß╗ü qu├í khß╗⌐ v├á **x├│a bß╗Å/viß║┐t lß║íi lß╗ïch sß╗¡** commit. C├íc commit ph├¡a sau vß╗ï tr├¡ reset sß║╜ bß╗ï t├ích khß╗Åi nh├ính.
  - `git revert` giß╗» nguy├¬n to├án bß╗Ö lß╗ïch sß╗¡ c┼⌐ v├á **tß║ío th├¬m mß╗Öt commit mß╗¢i** c├│ nß╗Öi dung ─æß║úo ng╞░ß╗úc ho├án to├án (inverse diff) c├íc thay ─æß╗òi cß╗ºa commit/merge commit muß╗æn hß╗ºy bß╗Å.
- **L├╜ do phß║úi d├╣ng revert tr├¬n master v├á release/*:**
  - **Bß║úo to├án m├┤i tr╞░ß╗¥ng cß╗Öng t├íc (Public branch safety):** Nh├ính `master` v├á `release/*` l├á nh├ính d├╣ng chung m├á c├íc th├ánh vi├¬n kh├íc trong nh├│m ─æ├ú ─æß╗ông bß╗Ö (`pull`) vß╗ü m├íy cß╗ºa hß╗ì. Nß║┐u ta d├╣ng `reset` rß╗ôi cß╗æ t├¼nh force push (`push --force`), c├óy lß╗ïch sß╗¡ cß╗ºa c├íc th├ánh vi├¬n kh├íc sß║╜ bß╗ï lß╗ùi lß╗çch gß╗æc, g├óy hß╗ùn loß║ín v├á nguy c╞í mß║Ñt code nghi├¬m trß╗ìng.
  - **T├¡nh truy vß║┐t (SCM Audit & Traceability):** Trong quß║ún l├╜ cß║Ñu h├¼nh chuß║⌐n, mß╗ìi h├ánh ─æß╗Öng sß╗¡a ─æß╗òi hay thu hß╗ôi ─æß╗üu phß║úi ─æ╞░ß╗úc ghi vß║┐t r├╡ r├áng. `git revert` tß║ío ra mß╗Öt commit ghi nhß║¡n minh bß║ích nguy├¬n nh├ón ho├án t├íc (v├¡ dß╗Ñ: revert PR bß╗ï lß╗ùi), gi├║p ─æß╗Öi ng┼⌐ kiß╗âm to├ín cß║Ñu h├¼nh nß║»m r├╡ tß║íi sao mß╗Öt thay ─æß╗òi tß╗½ng ─æ╞░ß╗úc t├¡ch hß╗úp rß╗ôi lß║íi bß╗ï thu hß╗ôi.

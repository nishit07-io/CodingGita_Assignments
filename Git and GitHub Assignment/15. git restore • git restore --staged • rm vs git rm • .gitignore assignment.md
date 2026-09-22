## Assignment 1 – Practice `git restore` and `git restore --staged`

**Goal:** Understand how staging and unstaging works with `git restore`.

1. Create a new file named `profile.txt` and write 3–4 lines about your favorite programming topic.
2. Run `git status` and note that the file is **untracked**.
3. Try the command:
```bash
git restore profile.txt
```
Observe that it does **not** work (because the file is untracked).
4. Stage the file:
```bash
git add profile.txt
```
5. Unstage it using:
```bash
git restore --staged profile.txt
```
6. Run `git status` again and confirm the file is back to untracked / unstaged.
7. Now stage and commit the file properly:
```bash
git add profile.txt
git commit -m "Add profile.txt"
```

**Submit:**
- Screenshot of `git status` when the file was untracked
- Screenshot after using `git restore --staged`
- Repository link

---

<img width="557" height="440" alt="WhatsApp Image 2026-09-07 at 9 59 50 PM" src="https://github.com/user-attachments/assets/86d24370-968c-4066-befe-59b6c76c84e9" />

<img width="749" height="859" alt="WhatsApp Image 2026-09-07 at 10 01 28 PM" src="https://github.com/user-attachments/assets/d4bc1dd3-960d-45e4-880e-9e2a480d8d20" />
## Assignment 2 – `rm` vs `git rm`

**Goal:** Understand the difference between normal delete and Git delete.

1. Make sure `profile.txt` is committed on `main`.
2. Delete the file using normal system command:
```bash
rm profile.txt
```
3. Run `git status` and observe the output.
4. Recover the file using:
```bash
git restore profile.txt
```
5. Now delete it properly with Git:
```bash
git rm profile.txt
```
6. Run `git status` again and observe the difference.
7. Commit the deletion:
```bash
git commit -m "Remove profile.txt using git rm"
```
8. Create a short file named `delete-difference.txt` and write in your own words:
- What is the difference between `rm` and `git rm`?
- When should you use `git rm`?

**Submit:**
- Screenshots of `git status` after `rm` and after `git rm`
- Content of `delete-difference.txt`
- Repository link

---

<img width="718" height="869" alt="WhatsApp Image 2026-09-08 at 8 08 10 AM" src="https://github.com/user-attachments/assets/a92606b8-38f4-4981-b7fc-fd654120d92b" />


<img width="728" height="869" alt="WhatsApp Image 2026-09-08 at 8 09 06 AM" src="https://github.com/user-attachments/assets/0dae50d7-8e9a-494f-b3f2-1025b160002d" />
Github link :- https://github.com/Sumitkumar196/git-stash-command

## Assignment 3 – `.gitignore` + `git rm --cached`

**Goal:** Properly ignore sensitive files and practice stopping Git from tracking a file using `git rm --cached`.

1. Create a file named `config.env` with sample secret data:
```env
DB_PASSWORD=SuperSecretPass999
API_KEY=sk-test-abc123xyz789
```

2. **Intentionally** add and commit it (to practice the fix):
```bash
git add config.env
git commit -m "Accidentally commit config.env"
```

3. Create a folder named `vendor` and put any dummy file inside it.

4. Create a `.gitignore` file and add:
```gitignore
vendor/
config.env
```

5. Stop tracking `config.env` but **keep the file on your computer**:
```bash
git rm --cached config.env
```

6. Run `git status` and observe that `config.env` is staged for removal from Git (but the file still exists locally).

7. Commit the fix:
```bash
git add .gitignore
git commit -m "Stop tracking config.env and add .gitignore"
git push origin main
```

8. Confirm on GitHub that `config.env` is **no longer visible** in the repository, while the file still exists on your local machine.

9. Create a file named `why-gitignore.txt` and answer:
- Why should we ignore folders like `vendor` or `node_modules`?
- Why should we ignore files like `config.env` or `.env`?
- What does `git rm --cached` do?
- Why should we **not** add `.gitignore` inside `.gitignore`?

**Submit:**
- Screenshot of `git status` after using `git rm --cached`
- Screenshot showing that `config.env` is ignored / removed from GitHub
- Content of `why-gitignore.txt`
- Repository link (make sure `config.env` is **not** visible on GitHub)


- <img width="727" height="911" alt="WhatsApp Image 2026-09-08 at 8 47 19 AM" src="https://github.com/user-attachments/assets/a3e5fced-11ee-48f5-87a7-5c3deabb2d29" />

<img width="750" height="836" alt="WhatsApp Image 2026-09-08 at 8 50 31 AM" src="https://github.com/user-attachments/assets/3b134d44-3707-4611-9a72-78af607ad802" />

<img width="1381" height="346" alt="WhatsApp Image 2026-09-08 at 8 57 05 AM" src="https://github.com/user-attachments/assets/9533b9e1-1f69-4154-8dfb-cf3f14f35f22" />

Github link :- https://github.com/Sumitkumar196/git-stash-command



Extract the following fields from the provided PDF or text file and output a single-line TSV (tab-separated) string in this exact order:

**Order of fields (must be strictly followed):**

```
Name Candidate	Source	Country	Channel Communication	Email	Phone	Telegram	Status	Last Contact Date	Department	Profession	Language	Language level	Job Application Link	Портфолио	Portfolio1	Portfolio2	Portfolio3	Portfolio4	Portfolio5	Portfolio6
```

---

### **Strict extraction and formatting rules:**

1. **Name Candidate** → Write in English only. Full name as written in the CV (first + last).
2. **Source** → "Djinni" for designers/developers, "Work.ua" for managers/leadgen, "robota.ua" for graphic designers.
3. **Country** → Always "Ukraine" unless another country is explicitly mentioned.
4. **Channel Communication** → Always "Telegram" if a telegram username/link is found. If not, but WhatsApp is found → "Viber". If no contact → leave empty.
5. **Email** → Extract from CV or text. If missing → leave empty.
6. **Phone** → Digits only, without "+", spaces, or brackets. If missing → leave empty.
7. **Telegram** → Write the handle (with @). If not found → leave empty.
8. **Status** → Always "Application".
9. **Last Contact Date** → Always today’s date in **DD-MM-YYYY** format. 14/10 - пиши текстом типу 13-10-2025
10. **Department & Profession** → Must strictly match allowed list:

* developers: back end developer, front end developer, full stack developer, mobile developer, system administrator, qa
* designers: ui/ux designer, web designer, graphic designer, 3d designer, illustrator
* marketers: smm manager, seo manager, ppc specialist, copywriter, media buyer, linkbuilder, email marketer, influencer manager, content manager, pr manager, affiliate manager, proofreader
* managers: hr manager, sales manager, recruiter, account manager, project manager, chat operator, personal assistant, tourism manager, investment manager, financial manager, event manager, lead generator
* videographers: video editor, motion designer, mobile video editor, animator
* linguistics: translator
  If not matching → leave both fields empty.

11. **Language** → Always "English".
12. **Language level** → Always "B1".
13. **Job Application Link** → Take the main profile/job application link (work.ua/djinni/robota.ua). If missing → leave empty.
14. **Портфолио** → Extract portfolio link (Behance/Dribbble) is found, place here. If not → leave empty.
15. **Portfolio1** → Extract all additional links (LinkedIn, GitHub, Google Drive, extra Behance/Dribbble, personal sites, PDFs). If fewer links exist → leave remaining cells empty.
**Portfolio2** → Extract all tools
**Portfolio3** → Extract all courses
**Portfolio4** → Extract all languages
---

⚡ **Output requirement:**

* Respond using **only one single-line TSV string** inside a code block (no explanations, no extra formatting).
* Always keep the exact order of columns listed above.
* If a field is missing → leave the cell empty (no `-`).



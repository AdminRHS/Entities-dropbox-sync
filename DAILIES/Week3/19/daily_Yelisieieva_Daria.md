Scoped the environment: mapped the whole Nov25 tree plus ENTITIES/DAILIES, listed available processing scripts, and confirmed the Processed/ outputs to understand how Nov 17–18 dailies are structured before touching data.
Audited employee folders across AI, Design, Dev, Fin, HR, LG, Sales, and Video: counted existing daily.md files for 17/18, gathered byte sizes via wc -c, and noted where folders existed but files were empty or missing.
Normalised data sources: fixed the ENTITIES/DAILIES/scripts/config.json path references, attempted the Dailies pipeline, and ultimately worked directly against the Nov25 employee folders when the pipeline paths proved unreliable.
Renamed mislabelled folders (e.g., Bessarab Valeriiia → Bessarab Valeriia, Rekonvald Viktoriia → Rekonvald Viktoriya) so employee IDs matched reporting outputs.
Produced FINAL_employee_coverage_detailed_analysis.md, which focuses on the 29 Work/Available/Part-Time employees, ranks coverage (20 complete, 9 partial/empty, 5 fully missing), and highlights the 10 problem cases with action priority.
Extracted and delivered the problem-employee list from that report (critical, high, medium tiers) per the user’s follow-up request.
Authored ENTITIES/DAILIES/FUTURE_NEEDS_AND_NEXT_STEPS.md, outlining Phase 1–4 follow-up work: syncing with days-off logs, building an all-files inventory (not just daily.md), merging findings into remediation plans, and suggesting process improvements.


Там приложили на лидогенерации баги, с бонус тем, кто преподаёт. То есть ты кому-то что-то объясняешь, получаешь 50 геймбонусов. Ну автоматизация понятна, что через N8N можно сделать, чтобы прямо оно подтягивалось, допустим, когда появляется новый звонок, чтобы оно всё было актуально. Но пока можно точно так же делать, как я делаю с Employees. Паблик со статусами, с рейтами, да? С актуальностью. Вот. И я вытянула такой же список именно по звонкам.  Смотри я сделала Звонки именно Active Staff то есть оно мне проанализировала тех людей которые есть здесь в списке Employees паблик С моим списком всех звонков И именно по этим людям. Сколько у кого?  Состояние на вот восемнадцать есть допустим  Я объединила прямо тут с начала года если нужно я сделаю отдельно  чисто на конкретный месяц просто я сделала этот документ с тем чтобы можно было его обрабатывать то есть ты вот ну а что у нас было в апреле три звонка в маркет база не может смотри там Active Staff то есть это те люди которые на сегодняшний день работают в компании они в фирале например ну как бы ну что-то не то это неплохой показатель ну я говорю можно добавить общее количество но я к тому не скучну я сделала так чтобы в карточке тех людей которые сейчас у нас активны чтобы оно взяло эту информацию допустим да и добавило что там допустим у ФРЗ допустим да было там для продвижения дела чуть-чуть путает хорошо я поэтому тебе вчера и написала что надо подумать как его ну как бы какие-то можно общие данные плюс можно же вытянуть данные ну да надо развивать зачем нам тут список тех сотрудников которых уже в помине нет да тут у нас был там Иваненко Кузина что они там кучу звуков назначали сейчас же нам это уже не сильно актуально в принципе можно добавить просто Total да по месяцам Total и можно Total по странам можно Total по индустрии а можно Total на Тотре в общем я буду это доделывать я думаю что в принципе документы можно будет обновлять каждый день просто ручками загрузить файл свежий его как бы так актуализировать а потом уже автоматизацию сделать.

So the next version of this automatization should include Following requirements:
1. We need to add the total of all calls made by all lead gens, regardless of their status. It wouldn't be only active staff without detailing just numbers for example total amount of calls for January, February etc.
2. We need to add the country of each call, industry for example so it would include total calls not only the calls of active staff.

Создание автоматизации на n8n для выгрузки данных из Google Sheets и попадание их на Dropbox. Ниже будет полный tutorial, как мы сделали эту автоматизацию 

 Create Workflow? Да. Create Workflow. Create Workflow. Ок. Так. И что ты хочешь там? Я хочу, чтобы из моего большого файла Google Sheets вынимала нам одну вкладку. Например, у нас есть "bonus analytics". Есть вкладка со звонками лидгенов. Но это очень скудные данные, вот эта, например, "Calls". И она ж постоянно типа дополняется. Вот когда только новые звонки появляются, мы дополняем тот файл, он постоянно стёрт, эта вкладка, ну короче, выполняется данными. Здесь у нас есть дата, компания, вот Lead Gen Manager, ID-шка, страна, индустрия. Это то, что мы с Колей сегодня обсуждали, чтобы можно было вытягивать данные по, ну типа, статистику по каким странам были, типа, звонки, сколько звонков. В общем, то есть привязка. Вот мне нужно сделать. Обычно, как я делаю, я просто сохраняла, типа, CSV документ на Dropbox, и уже оттуда автоматизации я его в markdown файл, типа, актуализировала и складывала в Control Box в Public. Получается, вот здесь есть папочка, вот это public и вот "Lead Gen Calls by Month". Ну, его надо еще переделать, потому что тут данные без страны и без индустрии. В принципе, вот сюда же можно его и заливать. Прямо вот этот, наверное, вкладку нужно с какой-то периодичностью, типа, обновлять и загружать на Dropbox, а уже из нее потом обработку включаем. То, что ты тут надиктовала, я тоже пишу. Значит, заходи туда, нажимай сюда, add first step. Тебе надо Trigger on you. Третий? А третий? А он с кем? Тут выбери раз в какой промежуток чего он будет читать твою таблицу. Пусть будет раз, два, часа три. Ладно, хорошо, все, закрывай все. Add rule? Не, не надо, это правило для триггера. Просто назад или на пустое место где-нибудь за этим окном. Теперь на плюсик рядом нажимай. Так, пиши тут Sheets Google? Да, append row in sheet. Вот теперь открывай еще одно окно в браузере, да, из под аккаунта Ника. Давай. Ой, пиши тут Google консоль. Она перекидывает. Не знаю, может, потому что у тебя Windows не активирована. Я сделаю сейчас по-другому. Сейчас мы его... У меня же есть тут Niko. Так, перенесла на н. Ву се э э? Так?

Отлично. Теперь возвращайся в опять три палки. Apis and services, OAUS. Вот это, да? Ага. А, credentials, извини. Credentials. А потом OAUS-05, да. Вверху create credentials. Это не наши. Это кто-то делал 13 марта. OAUS Plant ID. Выбирай здесь Web Application. Первое. Пиши имя. Как ты хочешь, чтобы называлось. Желательно, чтобы совпадало с названием ворклайфа. Флоу в n8n, чтобы ты понимала, откуда вы и куда. Там просто финн у меня на… Ну тогда пиши n8n finn sheets api… N8n finn sheets api. Можно просто sheets. Ага, давай ниже. Теперь вернись в н8н, заходи, а тут админ. Тебе надо ника. Ой-ой-ой, Даша! Я ещё не видела так. Finn my workflow можешь сразу переименовать в то, что ты хочешь, чтобы он назвался. Будет лежать у тебя в папке. Что там? Лг колс коллектор какой-то. И нажимай first step, добавляй триггер schedule. Да, on the schedule, да? Да-да. И раз во сколько должен слушать твой таблицу? На пустое место на плюсик sheets. Pen drawing sheet. Pen throwing sheet, да? Да-да. Credentials to connect. Нажимай на select credentials. О, ща подожди, надо виспер ставить.

Поднимись на самый верх. Так, ОАУС 2. Да. Google Sheets Account 2. Переименуй. Где? Где? Сверху слева. Google Sheets Account 2. Что это? Фин. Google Sheets. Фин. Как-то. Позначит, что это аккаунта НИКО для финансов создавался А, Фин опять не… Ну, как-нибудь… Да, видишь, ОАУС Redirected… url забирай это "Клик ту копи"? Да, "клик ту копи". Зайди обратно теперь туда же "Add url"? Ниже редирект "Авторайз редирект" вот сюда "Add" вставляй. Да. Сейчас то я гляну у себя, в верхней тоже Канада что ли? Ну, тут обязательно мы все сделали, тут необязательно. Сейчас минуту. Я колю разбудила получается, да? Скорее всего, да. Блин, а ничего мы туда не вставляем? Да, давай "Create". Его же потом поправить можешь после чего? Сейчас никуда не клацай. Никуда. Аккуратно "Client ID" копируй. Возвращайся в этот vm8n. В "Client ID" его пихай. Теперь спустись пониже, здесь "Client Secret". Возвращайся туда на консоль, вот тут пониже "Client Secret" видишь? Тоже копировать кнопочка. Все вставляй и мне тоже относятся все вот эти с подписями с заголовками, тоже вот эти все ключики. Да, я не хочу тогда посохранять, потому что потом ты его не увидишь, он не даст посмотреть уже. Да? Хорошо. Да, надо обязательно. Как его обозвать? n8. Я тут. Все. Так это скопировали и раскопировали. А теперь "Sign in with Google" надо нажать. А стой, вернись на консоль, нажми там "ok", потом создал "Offline Creep Created". Отлично, вот теперь возвращайся, можно штыкать сюда "Sign in with Google". Расколли, наверное, опять надо будет подтвердить тебя. Make sure you trust rushfin automation. Hello? Ну ты ее что, сама создала, поэтому ты ее "trust". Connection successful. Так и сфули, он у тебя зелененьким подсветилась уже аккаунт конец. Все, нажимай здесь на хрестик. Внизу там ничего он тебе больше не предлагал? Наверно, ничего. Вроде нет. Так, все. "Sheets with documents can't roll", вот он from lib. Нет, сейчас виспит.

Ой, дай бог памяти. Напиши convert. Convert file. Json. Options. Так, а зачем нам конвертировать, если мы его можем вытянуть? Или мы его не можем так сделать? Нет, не можем. Нам надо… Тут у тебя… Да. Куча разных отдельных переменных, а тебе это надо запихнуть в array, в массив json, и потом один файл, полученный, ты будешь закидывать на Dropbox. Поэтому Convert to json нам нужен. All items in that one file, да, output data, да, options, нажми add option, добавь файл name, как ты хочешь, чтобы он назывался. Вот конечный файл, который мы будем лить на Dropbox. Так, а у чего ты можешь будет добавлять какой-нибудь там? Название Google Sheets json ты прокарал. Как у тебя Google Sheets называется? Вместо calls, то есть он calls нижнее подчеркнение три хештега json. Вот input field, видишь, ты можешь перетащить. Ну ладно, можно поиграться, не это хорошо. Но не так. Calls точка и потом json, сразу формат укажем, а оно получится calls json точка json. Нет, оно получится без формата. А, да, так, все, нажми execute step, сейчас посмотрим, как он собирает это все в один array. Вот он. А ну, нажми view. Теперь нажал, вот он, готовый чистый массив джейсона со всеми данными. Хорошо, теперь добавляю еще плюсик, закрывай это все. Так ты была права, calls можно было просто ставить calls. Он точку джейсон потом сам подставляет. Так и Петру сдвину, жмакай на плюс, а там надо схватить и потянуть эту доску в сторону, тогда ты будешь двигаться. Ой, нормально, нормально, на плюсик Dropbox, вот так просто, тут прям upload file. 

вставлять сюда за пабликом? Да. Вставляю за пабликом. Нажми \*\*Expression\*\*. Сверху, с \*\*Fixed\*\* на \*\*Expression\*\*, да. А ничего, что-то эти, так, что-то страшное ты скопировала? А, да, сейчас. Просто сюда в чат скину. А я забыла в твоей Украине сообщение просто. Чат открыть получается? Уже в чат скинул. Ага! А ничего тут пробел? В начале открой 2 фигурные скобки и пробел перед \*\*NOV25\*\*. Фигурные скобки! Чифт что? \*\*H\*\*. Буква \*\*H\*\*. А все. И пробел? Вот так? Да, должно было быть так. А что-то не хочет. Нажми вот тут внизу куда-нибудь, чтобы это схлопнулось на свободное место внутри этого окна. На нажми на кнопочку \*\*binary file\*\*. Сюда? Да! \*\*Data\*\*! Чего она пишет именно? Не хочу, чтобы она \*\*data\*\* называлась! Ну ладно, эээ хорошо, ээ оставь только \*\*NOV25\*\*, В \*\*25\*\* слэш \*\*финнов\*\* \*\*25\*\* слэш \*\*паблик\*\* слэш Сотри все что ты только что добавила короче. Скобки и фигуры надо оставлять? Не, не, не, можешь тоже убрать. Мы сейчас переключимся на \*\*fix it\*\* выражение и спереди смотри полностью всё, ага, лишнего пробела там не оставила после \*\*public\*\* слэш не оставила. Переключись на \*\*fix it\*\*, ага, нажми \*\*execute\*\*. Вдоль нас таб, да, да, да, под \*\*request didn't match pattern no parameters argument pas did not match pattern\*\*. А извини, поставь слэш перед \*\*NOV25\*\*, надо чтобы со слэшом начиналось, ага, и еще \*\*execute\*\*. Степ подожди, как у меня мэтчимся? Ааа, а че у тебя слышит не в ту сторону? Ну это я знаю, у меня постоянно так копируется почему-то из \*\*дробокса\*\*. Я хотела спросить, может в другую сторону можно поменять, взять другую сторону? У тебя так копируют все, да? Да! Я не понимаю, что это за \*\*и\*\* в серединке, а там поменяно, да, уже окей, давай попробуем. \*\*Your request is invalid would not be preceded by the service pass\*\*. А ну открой \*\*error details from dropbox\*\*. А видишь что тут? Ой, пути путя не знаю. Ну видишь, что тут эти слэши разные стороны. Снова-таки, в принципе, что нам тут это именно уже получается в \*\*DropBox\*\*, чтобы она положила правильно? Да! Это чтобы он положил \*\*DropBox\*\*. Может, я это скопирую и потом поиграюсь с ним. Почему такая ошибка? Сейчас добьём. \*\*Your request is invalid would not be preceded by the service\*\*. Продолжение

Она там создалась с этим. Да. Есть. Получили. Молча сон весь в одну строку. Видишь? Это он по умолчанию так, да? Ложит, получается? Да. По умолчанию вот так ложит. Поэтому. Ой. Это пошла синхронизация. Твой скрипт разрабатывается. Я ничего, я это тоже перекину потом на N8N. Ну теперь можно посидеть с Иишкой и попросить его, чтобы он этот массив из одной строки располпили по разным строчкам или перевел в Markdown. Ну да, в Markdown или в каком там тебе формате. Ну вообще у меня все документы в Markdown'ах. Я думала, я Коль, а в каком нам формате нужен этот документ в Markdown'е? Ты меня спрашиваешь? Да. А какой нам именно документ, о каком документе речь? Это звонки ледгенов, откуда помнишь, мы хотели забирать. Ну да, но там есть еще какой-то секретный, я не знаю, где он находится, но есть Коробочка AI Agent, агент, который ты можешь прикреплять, пару щупальцев. И ты можешь ему просто отдать эти данные, а потом из него уже стрелочку сделать, куда тебя в Dropbox переподсоединить, вот эти ветки через коробочку. А в коробочку подключить токены искусства интеллекта. Он тебе хочет будет упорядочивать, хочешь другие форматы и прикрепить. Ну что ему, ты ему там в промке скажешь? То и можно сделать. А нам в любом случае, в любом варианте подойдет JSON, Markdown. Ну в принципе, это же исходные данные, мы же их потом будем еще обрабатывать. То есть нам же надо будет из него вытащить, допустим, статистику по количеству по странам, по количеству по ледгенам, то есть ну разные. В любом формате закидывая, хоть даже от все одной строчки, лишь бы они попали на Dropbox. Только они попадут, там уже не вопрос. Ну замечательно. А вообще такие штучки, по идее, и GPT в GPT есть коннектор к N8M. Ну может не к нашей локальной модели, но они в идее и Gemma GPT, и Кло, тебе вот эти вот все коробочки, когда ты описываешь, что тебе надо, ты там нажимаешь импорт, все эти коробочки, и потом самое сложное — это вот эти вот все ключи поставить, что Коля сказал. То есть на этих коробочках, то не проблема. Ну вы большие молодцы, конечно. Это Коля все, спасибо Коле большое. Я же могу потом по аналогии, да, попробовать сделать, допустим, другую. Вот то, что я делаю, например, вот так сижу, у меня в одном окне тут Gemini, можешь любой другой использовать. Мы с ним вот сидим и рассказываем то, что я не знаю, просто прошел, я запомнил. А ты можешь все браузер вот это мид открыть, и прямо тогда он видит твоё окно, и ты его можешь прямо спрашивать, куда дальше. Ну или Атлас на Маке пока только нет, да? Ну извините. В общем, уже очень хорошо, я думаю. Спасибо большое. Первая победа, а там уже хочешь письма, можешь отправлять. Ты можешь там, как только у тебя появился еще один звонок, то отправь ему письмо с Новым годом. Зайди в список сотрудников с имейлами в Dropbox и найди имейл, и напиши ему письмо: "Поздравляю". Не, но это ты уже забежал. Я надеюсь так сделать эти задания на завтра. Мне каждый день кажется, что я все уже сейчас допилил, и все, сейчас оно прямо за поет. Ну вот, надеюсь завтра. Я хочу попробовать сделать, значит, то же самое вот с этим с эмплаизмом, который вот у меня вручную получается. Ну не вручную, но по графику именно с моего ноутбука синхронизирует. А можно же точно так же через n8n переключить, чтоб она убрала уже тоже с Google Sheets. Я, короче, попробую, если получится. А она синхронизируется типа из Dropbox, из файла, который у тебя лежит в папке, а так она будет прямо, я получается его, ну мануально зираю, когда вношу какие-то данные новые, и оно у меня уже потом синхронизируется по гра, по этому, по скеджу. Там же ж можно будет и в обратную сторону, если что, можно в Google записывать там что-то другое, третье. Так что там полет фантазии. Ну короче, это просто прорыв, я считаю, да.

То есть, ты инструкции позаливала свои ежедневные процессы описания. Он тебе дает 50 вариантов, и ты уже играешься, какие тебе нравятся. 

Ну, понятно, надо брать по приоритетам то, что нам важнее сейчас. Опять-таки, чтобы оно все было в одном месте — информация, которая вот как ты хочешь. 


Overview
You created an N8N workflow to automatically export data from a Google Sheets table ("Calls" sheet) to Dropbox as a JSON file. This enables regular automated data collection without manual downloads.
Steps Completed:
1. Initial Setup & Workflow Creation
Created a new workflow in N8N
Named it descriptively (e.g., "LG Calls Collector") to track where data flows from/to
2. Set Up Google Sheets API Authentication
Created OAuth2 credentials in Google Cloud Console under Credentials
Named the credentials "n8n finn sheets api" to match the workflow purpose
Set up proper redirect URIs in Google Cloud
Generated and saved Client ID and Client Secret
Authenticated the connection in N8N with "Sign in with Google"
3. Configured the Workflow Triggers & Steps
Trigger: Set Schedule trigger to read the Google Sheets table every 3 hours (configurable)
Step 1: Added "Get All Rows" from Google Sheets to pull data from the "Calls" sheet
Step 2: Added "Convert to JSON" node to transform the data into a single JSON array format
Configured output filename as "calls.json"
Step 3: Added Dropbox "Upload File" node to save the JSON file
4. Path Configuration
Set Dropbox upload path to: /NOV25/Fin Nov25/public/ directory
This allows the JSON file to be stored in your public folder for further processing
Result
✅ Successful Automation Created:
The workflow now automatically exports your Google Sheets "Calls" data as a JSON file to Dropbox every 3 hours
The data includes: Date, Company, Lead Gen Manager, ID, Country, and Industry information
The file is ready for further processing (conversion to Markdown, analysis, etc.)
Next Steps Discussed
Future enhancement: Convert the JSON output to Markdown format for your documentation
Possibility to expand this approach to other data sources (like Employee data)
Integration with AI agents to format and analyze the data further
Potential to add email notifications when new calls are recorded
This automation replaced your previous manual CSV export process with a scheduled, hands-free solution!

---

## TUTORIAL: How to Create N8N Workflows for Google Sheets to Dropbox Export

This tutorial provides step-by-step instructions to create similar automation workflows for any Google Sheets to Dropbox export. Use this guide when you need to set up new workflows for different data sources.

### Prerequisites
- N8N account access
- Google Cloud Console account access
- Dropbox account access
- Read/write permissions to the Google Sheets you want to export
- Dropbox folder path where you want files saved

---

### PART 1: Setting Up Google Cloud API Credentials

#### Step 1: Access Google Cloud Console
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Log in with the Google account that has access to your Sheets

#### Step 2: Create OAuth 2.0 Credentials
1. In the left sidebar, click **APIs and Services**
2. Click on **Credentials**
3. Click the blue **+ Create Credentials** button at the top
4. Select **OAuth client ID**
5. If prompted, first configure the OAuth consent screen:
   - Click **Configure Consent Screen**
   - Choose **External** user type
   - Fill in the application name and your email
   - Add the required scopes
   - Save and continue

#### Step 3: Configure the OAuth Application
1. Return to **Create Credentials** > **OAuth client ID**
2. Select **Web Application** as the application type
3. Enter a descriptive name: `n8n_[workflow-name]_sheets_api` (e.g., `n8n_calls_sheets_api`)
   - This helps identify which N8N workflow uses this credential
4. Under **Authorized redirect URIs**, click **Add URI**
5. Copy the redirect URI from your N8N workflow (you'll get this in Part 2, Step 4)
6. Click **Create**

#### Step 4: Save Your Credentials
A modal will show your credentials. **Important: Copy and save these immediately:**
- **Client ID** - needed for N8N
- **Client Secret** - needed for N8N (you won't be able to see it again)
- Store these securely; you'll paste them into N8N

---

### PART 2: Creating the N8N Workflow

#### Step 1: Create and Name Your Workflow
1. Log into your N8N instance
2. Click **Create Workflow**
3. Rename the workflow to something descriptive: `[Source]_to_Dropbox_[Schedule]`
   - Example: `LG_Calls_to_Dropbox_Hourly`
4. This becomes the folder name where your workflow is stored

#### Step 2: Add a Schedule Trigger
1. Click **Add first step**
2. Search for and select **Schedule** trigger
3. Configure the schedule:
   - Choose interval: Hourly, Every 3 hours, Daily, etc.
   - This determines how often the export runs
   - Example: Select "Every 3 hours" to export every 3 hours

#### Step 3: Connect Google Sheets
1. Click the **+** button to add a new node
2. Search for and select **Google Sheets**
3. Choose **Get All Rows** action
4. For credentials:
   - Click **Create New Credential**
   - Or select **Select Credentials** if one exists
   - Name it: `Google Sheets - [Account Purpose]` (e.g., `Google Sheets - Fin`)

#### Step 4: Authenticate with Google
1. Click **Sign in with Google**
2. A window will open - log in with the account that owns the Sheets
3. Accept the permission request ("Make sure you trust n8n automation")
4. You should see "Connection successful" confirmation

#### Step 5: Select Your Google Sheet
1. In the Google Sheets node, select:
   - **Spreadsheet ID** - paste or select your Google Sheets document
   - **Sheet Name** - select the specific sheet tab (e.g., "Calls", "Employees")
2. Click **Execute Node** to test and preview the data

#### Step 6: Convert Data to JSON
1. Click **+** to add another node
2. Search for and select **Convert** (or look for "Convert to JSON")
3. Configure:
   - **Input**: Select "All items in one file"
   - **Output Data**: Ensure "Output data" is selected
   - Click **Add Option** and select **File Name**
   - **File Name**: Enter your desired output name without extension (e.g., `calls` → will become `calls.json`)
4. Click **Execute Node** to verify it creates a proper JSON array

---

### PART 3: Uploading to Dropbox

#### Step 1: Add Dropbox Upload Node
1. Click **+** to add another node
2. Search for and select **Dropbox**
3. Choose **Upload File** action
4. For credentials:
   - Click **Create New Credential** or select existing
   - Authenticate with your Dropbox account

#### Step 2: Configure the Upload Path
1. **Path** field: Click to switch from **Fixed** to **Expression**
2. Enter your Dropbox folder path in the format:
   ```
   /NOV25/Fin Nov25/public/[filename].json
   ```
   - Replace with your actual folder structure
   - **Important**: Path must start with `/`
   - Use forward slashes `/` even on Windows
3. **File Content**: This should auto-populate with data from the Convert node

#### Step 3: Test the Upload
1. Click **Execute Node**
2. Check your Dropbox folder to confirm the file was created
3. If you get path errors:
   - Verify the folder path exists in Dropbox
   - Ensure no trailing spaces or incorrect slashes
   - Use the error message to identify the exact issue

---

### PART 4: Finalizing and Deploying

#### Step 1: Test the Complete Workflow
1. Click **Test workflow** or **Execute** button at the top
2. Monitor all nodes to ensure no errors occur
3. Verify the JSON file appears in your Dropbox folder

#### Step 2: Activate the Workflow
1. Click the toggle in the top-left to **Activate** the workflow
2. Once active, the schedule trigger will begin executing at the intervals you set

#### Step 3: Monitor Execution
1. In N8N, view the **Executions** tab to see:
   - When the workflow ran
   - If it succeeded or failed
   - Error details if failures occurred

---

### Common Configurations for Different Use Cases

#### For Real-Time Data (Every Hour)
- Schedule Trigger: **Every hour**
- Use when data changes frequently and you need current information

#### For Daily Reports (Once Per Day)
- Schedule Trigger: **Daily at specific time** (e.g., 9:00 AM)
- Use for daily summaries or reports

#### For Large Spreadsheets
- May need to increase N8N timeout settings
- Consider daily or less frequent exports if the sheet is very large

#### For Multiple Sheets from Same Workbook
- Create separate workflows for each sheet
- Name them clearly: `Workbook_Calls_to_Dropbox`, `Workbook_Employees_to_Dropbox`, etc.

---

### Troubleshooting Guide

| Error | Solution |
|-------|----------|
| "Invalid credentials" | Re-authenticate with Google. Check that the Google account has access to the Sheets document. |
| "Sheet not found" | Verify the sheet name exactly matches the tab name in Google Sheets (case-sensitive). |
| "Path does not exist" | Create the folder in Dropbox first. Ensure path starts with `/` and uses forward slashes. |
| "Invalid file name" | Avoid special characters in the filename. Use only alphanumeric characters, underscores, and hyphens. |
| "Request didn't match pattern" | Check for extra spaces in the path. Verify the path format is correct (starting with `/`). |
| "File already exists" | The workflow overwrites existing files with the same name. This is normal behavior. |

---

### Security Notes

- **Never share Client ID or Client Secret** - these grant access to your data
- Store credentials only in N8N's credential manager
- Credentials appear as green when verified - do not copy/paste them elsewhere
- For team access, use N8N's credential sharing features rather than sharing passwords

---

### Next Steps After Basic Export Works

Once your basic export is running successfully, consider:

1. **Data Transformation**: Add nodes to filter, transform, or enrich the data before exporting
2. **Format Conversion**: Convert JSON to Markdown, CSV, or other formats using additional nodes
3. **Conditional Logic**: Use "If" nodes to handle different data based on conditions
4. **Multiple Destinations**: Send the same export to multiple Dropbox folders or other services
5. **Notifications**: Add email or webhook notifications when exports complete or fail
6. **Error Handling**: Add error recovery nodes to handle and log failures gracefully


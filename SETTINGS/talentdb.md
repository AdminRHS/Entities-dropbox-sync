Block	Tables	Columns	Data type	Comments
settings	entity_types	id	TINYINT	
settings	entity_types	name	VARCHAR(50)	
settings	entity_types	table_name	VARCHAR(100)	NULLABLE
settings	entities	id	TINYINT	
settings	entities	name	VARCHAR(100)	
settings	entities	table_name	VARCHAR(100)	
settings	entities	entity_type_id	TINYINT	NULLABLE
settings	entities	description	VARCHAR(500)	
settings	blocks	id	TINYINT	
settings	blocks	name	VARCHAR(100)	
settings	blocks	table_name	VARCHAR(100)	
settings	entity_block	id	SMALLINT	
settings	entity_block	entity_id	TINYINT	candidate
settings	entity_block	block_id	TINYINT	communication
settings	statuses	id	TINYINT	
settings	statuses	name	SMALLINT	
settings	statuses	color	VARCHAR(50)	
settings	status_entity_blocks	id	TINYINT	
settings	status_entity_blocks	status_id	TINYINT	
settings	status_entity_blocks	is_default	BOOLEAN	при совпадении статуса с entity_block дать возможность назначать is_default (тот который будет подставляться при создании определенной сущности). Если для одной сущности default уже выбран и назначается второй, то первый должен сбрасываться (так как status - single select) 
settings	status_entity_blocks	entity_block_id	SMALLINT	
settings	priorities	id	TINYINT	
settings	priorities	name	VARCHAR(50)	
settings	currencies	id	TINYINT	employees
settings	currencies	name	VARCHAR(50)	employees
settings	currencies	iso3	CHAR(3)	
settings	currencies	symbol	CHAR(3)	
settings	rates	id	TINYINT	
settings	rates	value	FLOAT	
settings	rates	name	VARCHAR(50)	
settings	rates	hours	SMALLINT	
settings	shifts	id	TINYINT	
settings	shifts	name	TINYINT	
settings	shifts	start_time	TIME	
settings	shifts	end_time	TIME	
settings	fields	id	SMALLINT	employees
settings	fields	db_name	VARCHAR(50)	
settings	fields	table_name	VARCHAR(100)	
settings	fields	front_name	VARCHAR(100)	
settings	fields	translation_id	TINYINT	
settings	entity_block_fields	id	SMALLINT	
settings	entity_block_fields	entity_block_id	SMALLINT	employees
settings	entity_block_fields	field_id	SMALLINT	employees
settings	entity_block_fields	is_mandatory	BOOLEAN	
settings	holidays	id	TINYINT	
settings	holidays	name	VARCHAR(255)	
settings	holidays	date	DATE	
settings	holidays	paid	BOOLEAN	
settings	holidays	country_id	TINYINT	
settings	calendars	id	SMALLINT	
settings	calendars	name	VARCHAR(100)	
settings	calendar_users	calendar_id	SMALLINT	
settings	calendar_users	user_id	SMALLINT	
settings	permissions	id	SMALLINT	
settings	permissions	name	VARCHAR(100)	
settings	permissions	display_name	VARCHAR(100)	
settings	permissions	description	VARCHAR(100)	
settings	permissions	entity_id	TINYINT	
settings	permissions	is_custom	BOOlEN	
settings	permissions	allowed_permissions	JSON 	
settings	permission_types	id	TINYINT	
settings	permission_types	name	VARCHAR(20)	
settings	roles	id	SMALLINT	
settings	roles	name	VARCHAR(100)	
settings	roles	display_name	VARCHAR(100)	
settings	roles	description	VARCHAR(255)	
settings	profession_permission	id	SMALLINT	
settings	profession_permission	profession_id	SMALLINT	
settings	profession_permission	permission_id	SMALLINT	
settings	profession_permission	permission_type_id	TINYINT	
settings	push_notifications	id	SMALLINT	
settings	push_notifications	name	VARCHAR(100)	
settings	push_notifications	slug	VARCHAR(100)	
settings	push_notifications	is_notification	BOOLEAN	
settings	user_notifications	id	MEDIUMINT	
settings	user_notifications	user_id	SMALLINT	
settings	user_notifications	push_notification_id	SMALLINT	
settings	user_notifications	is_notification	BOOLEAN	
settings	operators	id		
settings	operators	name	plus	
settings	operators	symbol	 +	
settings	operators	setting_id	SMALLINT	
settings	tooltips			
settings	tooltips			
settings	tooltips			
settings	dropdown_settings	id		
settings	dropdown_settings	entity_type_id	Job	Job
settings	dropdown_settings	entity_id	Job_application	Job_application
settings	dropdown_settings	block_id	Profile	Profile
settings	dropdown_settings	field_id	Profession	Status
settings	dropdown_settings	table_name	profession_id	status_id
settings	dropdown_settings	group	priority	Status type
settings	dropdown_settings	group_data	Main	Recruitment
settings	dropdown_settings	value	Main	Video, New, Follow-Up
settings	frequencies	id	TINYINT	
settings	frequencies	name	VARCHAR(50)	
settings	frequencies	frequency_type_id		
settings	frequencies	days_num	TINYINT	
settings	frequencies	day_of_week		
settings	frequencies	from	TIMESTAMP	
settings	frequencies	to	TIMESTAMP	
settings	frequency_types	id		
settings	frequency_types	name		daily, weekly, monthly, this week, last week. last 30 days
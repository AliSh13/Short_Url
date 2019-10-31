"""Запрос sql"""


create_table_url = '''
        CREATE TABLE URL(
        URL VARCHAR(512) NOT NULL,
        S_URL VARCHAR(80) UNIQUE NOT NULL,
        USER VARCHAR(80),
        COUNTER INT DEFAULT 0,
        CHROME INT DEFAULT 0,
        FIREFOX INT DEFAULT 0,
        SAFARI INT DEFAULT 0,
        OTHER_BROWSER INT DEFAULT 0,
        ANDROID INT DEFAULT 0,
        IOS INT DEFAULT 0,
        WINDOWS INT DEFAULT 0,
        LINUX INT DEFAULT 0,
        MAC INT DEFAULT 0,
        OTHER_PLATFORM INT DEFAULT 0 ,
        PRIMARY KEY(S_URL));
        '''
add_index = """
        ALTER TABLE URL ADD INDEX (URL);
        """
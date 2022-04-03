ALTER TABLE chat
    ADD COLUMN IF NOT EXISTS greeter JSONB DEFAULT
    '{"switch": true, "ru": "DEFAULT", "en": "DEFAULT", "ua": "DEFAULT"}'::jsonb;

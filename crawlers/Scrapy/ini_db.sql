CREATE TABLE IF NOT EXISTS "Obra" (
	"latitud"	REAL DEFAULT 0,
	"longitud"	REAL DEFAULT 0,
	"radio_error"	REAL DEFAULT 99999999,
	"n_gruas"	INTEGER DEFAULT 0,
	"direccion"	TEXT DEFAULT '???',
	"num"	TEXT DEFAULT '???',
	"cp"	TEXT DEFAULT '???',
	"provincia"	TEXT DEFAULT '???',
	"comunidad"	TEXT DEFAULT '???',
	"pais"	TEXT DEFAULT '???',
	"uso1"	TEXT DEFAULT 'otros' CHECK("uso1" in ('residencial', 'oficina', 'retail', 'terciario', 'hotel', 'otros')),
	"uso2"	TEXT DEFAULT 'otros',
	"obra_nueva"	INTEGER DEFAULT 1,
	PRIMARY KEY("latitud","longitud")
);

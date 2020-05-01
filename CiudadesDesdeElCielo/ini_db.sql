<?xml version="1.0" encoding="UTF-8"?><sqlb_project><db path="/home/ismavb/MyRepos/CiudadesDesdeElCielo/CiudadesDesdeElCielo/DB.sqlite3" readonly="0" foreign_keys="1" case_sensitive_like="0" temp_store="0" wal_autocheckpoint="1000" synchronous="2"/><attached/><window><main_tabs open="structure browser pragmas query" current="3"/></window><tab_structure><column_width id="0" width="300"/><column_width id="1" width="0"/><column_width id="2" width="100"/><column_width id="3" width="3600"/><column_width id="4" width="0"/><expanded_item id="0" parent="1"/><expanded_item id="1" parent="1"/><expanded_item id="2" parent="1"/><expanded_item id="3" parent="1"/></tab_structure><tab_browse><current_table name="4,4:mainObra"/><default_encoding codec=""/><browse_table_settings><table schema="main" name="Obra" show_row_id="0" encoding="" plot_x_axis="" unlock_view_pk="_rowid_"><sort/><column_widths><column index="1" value="53"/><column index="2" value="66"/><column index="3" value="87"/><column index="4" value="62"/><column index="5" value="71"/><column index="6" value="37"/><column index="7" value="28"/><column index="8" value="72"/><column index="9" value="85"/><column index="10" value="35"/><column index="11" value="39"/><column index="12" value="39"/><column index="13" value="89"/></column_widths><filter_values/><conditional_formats/><row_id_formats/><display_formats/><hidden_columns/><plot_y_axes/><global_filter/></table></browse_table_settings></tab_browse><tab_sql><sql name="SQL 1">drop table Obra;

CREATE TABLE &quot;Obra&quot; (
	&quot;latitud&quot;	REAL DEFAULT 0,
	&quot;longitud&quot;	REAL DEFAULT 0,
	&quot;radio_error&quot;	REAL DEFAULT 99999999,
	&quot;n_gruas&quot;	INTEGER DEFAULT 0,
	&quot;direccion&quot;	TEXT DEFAULT '???',
	&quot;num&quot;	TEXT DEFAULT '???',
	&quot;cp&quot;	TEXT DEFAULT '???',
	&quot;provincia&quot;	TEXT DEFAULT '???',
	&quot;comunidad&quot;	TEXT DEFAULT '???',
	&quot;pais&quot;	TEXT DEFAULT '???',
	&quot;uso1&quot;	TEXT DEFAULT 'otros' CHECK(&quot;uso1&quot; in ('residencial', 'oficina', 'retail', 'terciario', 'hotel')),
	&quot;uso2&quot;	TEXT DEFAULT 'otros' CHECK(&quot;uso2&quot; in ('residencial', 'oficina', 'retail', 'terciario', 'hotel')),
	&quot;obra_nueva&quot;	INTEGER DEFAULT 1,
	PRIMARY KEY(&quot;latitud&quot;,&quot;longitud&quot;)
);</sql><current_tab id="0"/></tab_sql></sqlb_project>

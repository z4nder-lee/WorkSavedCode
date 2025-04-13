import csv
import re

# Step 1: Load your CSV file of scraped names
extracted_presenters = set()
with open("EEAESEM2016_clean_presenters.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        extracted_presenters.add(row["Presenter Name"].strip())

# Step 2: Paste the participant list below
participant_text = """
1	Abbring, Jaap	P108, C108
2	Adamopoulos, Tasso	P213
3	Adao, Bernardino	P12
4	Adena, Maja	P126
5	Adermon, Adrian	P215
6	Adsera, Alicia	P223, C223
7	Aghion, Philippe	D1, C67, P277
8	Aguirre, Alvaro	P204, P366
9	Ahammer, Alexander	P43
10	Ahlgren, Niklas	P56
11	Ahnert, Toni	P76, C76
12	Aikman, David	P179
13	Akin, Nuray	P203
14	Aladysheva, Anastasia	P358, C358
15	Alcala, Francisco	P89
16	Aldama, Pierre	P115
17	Aldasoro, Iñaki	P76
18	Alessandri, Piergiorgio	P254
19	Alfaro, Laura	P70
20	Alogoskoufis, George	P153, C153
21	Alpman, Anil	P94
22	Altinoglu, Levent	P102, C102
23	altunok, fatih	C79, P239
24	Amador, João	P8
25	Amand, Marnix	P158, C158
26	Ambühl, Sandro	P72
27	Amengual, Dante	P202
28	Anagnostopoulos, Alexis	P59, C59
29	Anatolyev, Stanislav	P99, C99, P114, P168
30	Andor, Mark	P247
31	Andreottola, Giovanni	P135, C135
32	Andreyanov, Pavel	P199
33	Andrietti, Vincenzo	P211
34	Angeletos, George-Marios	P348
35	Antic, Nemanja	P199, C199
36	Antony, Jürgen	P114, C114
37	Anukriti, S	P23, C23, P157
38	Arefiev, Nick	P178
39	Ari, Anil	P188
40	Armenter, Roc	P253, C253
41	Armstrong, Mark	P67, P197
42	Arni, Patrick	P94, C94
43	Arve, Malin	P302
44	Asai, Yukiko	P89
45	Athias, Laure	P123, C123
46	Atmaca, Sümeyra	P112
47	Attanasi, Giuseppe	P22
48	Auriol, Emmanuelle	C66
49	aus dem Moore, Nils	P49
50	Auster, Sarah	P199
51	Avdjiev, Stefan	P3, C3
52	Aylar, Emre	P50
53	Ayouni, Mehdi	P30
54	Öhman, Mattias	P85
55	Babiak, Mykola	P175
56	Babii, Andrii	P314
57	Bacchetta, Philippe	P210
58	Bachmann, Andreas	P141
59	Backus, Peter	P251
60	Baeurle, Gregor	P12, C12
61	Bahaj, Saleem	P372, C372
62	Bai, Ying	P80
63	Balazsi, Laszlo	P50, C50
64	Baldwin, Richard	P70, P207
65	Ballester, Miguel-Angel	P162, C162
66	Bandiera, Oriana	C277
67	Banerjee, Priyodorshi	P109
68	Baqaee, David	P342, P383
69	Barattieri, Alessandro	P190, C190
70	Barboni, Giorgia	P244, C244
71	Barendse, Sander	P99
72	Bartalotti, Otavio	P206
73	Barth, Andreas	P286
74	Bartling, Bjoern	P72, C72
75	Barunik, Jozef	P131
76	Basak, Deepal	P53
77	Basso, Gaetano	P142
78	Basteck, Christian	P65, C65
79	Battisti, Michele	P294
80	Bauer, Michael	P304
81	Baziki, Selva	P17
82	Bedre-Defolie, Özlem	P263, C263
83	Beestermoeller, Matthias	P52
84	Beggs, Alan	P192
85	Bekierman, Jeremias	P235
86	Ben Yahmed, Sarra	P17
87	Benabou, Roland	P280
88	Benkert, Jean-Michel	P134, P316, C316
89	Bergemann, Annette	P43
90	Berlin, Maria	P284, C284
91	Berlingieri, Giuseppe	P221
92	Berman, Eli	P382
93	Bermperoglou, Dimitrios	P183, C183
94	Berniell, Lucila	P120
95	Bertay, Ata Can	P119
96	Bertoletti, Paolo	P315
97	Berzins, Janis	P367
98	Bessec, Marie	P235
99	Besstremyannaya, Galina	P303
100	Bianchi, Benedetta	P88
101	Bianchi, Daniele	P304, C304
102	Biasi, Barbara	P336, C336
103	Biewen, Martin	P211
104	Billio, Monica	P271, C271
105	Björklund, Maria	P46
106	Blasco, Sylvie	P151, C151
107	Blengini, Isabella	P117, C117
108	Blickle, Kristian	P86
109	Bloch, Francis	P234
110	Block, Juan	P371
111	Blundell, Richard	C1
112	Bobtcheff, Catherine	C302, C369
113	Boccanfuso, Jeremy	P360
114	Bocola, Luigi	P279, C279
115	Bodenstein, Martin	P142, C142
116	Bodory, Hugo	P127
117	Bojilov, Raicho	P300, C300
118	Bombaywala, Sama	P68
119	Bondarev, Anton	P78
120	Bonev, Petyo	P354
121	Bonfim, Diana	P182
122	Bonomo, Marco	P372
123	Bonomolo, Paolo	P100, C100
124	Boockmann, Bernhard	P120, C120
125	Boom, Anette	P180, C180
126	Boot, Tom	P137, C137
127	Bosio, Giulio	P359
128	Bossler, Mario	P324, C324
129	Bouakez, Hafedh	P84
130	Bourdieu, Jerome	P152
131	Bracke, Philippe	P86
132	Breckenfelder, Johannes	P159
133	Breckner, Miriam	P38
134	Bredemeier, Christian	P84, P174
135	Brendon, Charles	P47, C47
136	Brey, Bjoern	P335
137	Bridet, Luc	P176
138	Bripi, Francesco	P298
139	Britto, Diogo	P362
140	Britz, Volker	P208
141	Brown, Sarah	P242
142	Brown, Alasdair	P326, C326
143	Browning, Martin	P172, C172, P242
144	Bruell, Eduard	P89, C89
145	Bruins, Marianne	P23, P248
146	Brumm, Johannes	P25
147	Bruttel, Lisa	P316
148	Brutti, Zelda	P81, C81, P268
149	Brzoza-Brzezina, Michał	P186
150	Bucher, Anne	P16
151	Buehler, Stefan	P242, C242
152	Buetikofer, Aline	P236
153	Burgess, Stephen	P218
154	Burzynski, Michal	P223
155	Busse, Anna	P245, C245
156	Byrne, David	P252
157	Ca' Zorzi, Michele	P7, C7
158	Cacciatore, Matteo	P306
159	Cahlikova, Jana	P251, C251
160	Cairo, Isabel	P153
161	Cajner, Tomaz	P219
162	Calcagno, Riccardo	P176, C176
163	CALVO PARDO, Hector F.	P58
164	Camargo, Braz	P105
165	Canaan, Serena	P321
166	Canay, Ivan	P95
167	Caner, Mehmet	P237
168	Canidio, Andrea	P105, C105, P291, C291
169	Canova, Fabio	P386
170	Canta, Chiara	P330, C330
171	Cappelen, Alexander	P72
172	Carapella, Francesca	P253
173	Carre, Martine	P190
174	Carstensen, Vivian	P258
175	Carvalho, Carlos	P47, P101
176	Casarin, Roberto	P301
177	Cassou, Matthieu	P214
178	Cavaliere, Giuseppe	P24, C24
179	Cavicchioli, Maddalena	P131, C131
180	Cœuré, Benoît	D75
181	Celik, Gorkem	P128
182	Celik Katreniak, Dagmara	P350
183	Cerrone, Claudia	P20
184	Cesa-Bianchi, Ambrogio	P26, C26, P292, C292
185	Chabé-Ferret, Bastien	P113, C113
186	Chadi, Adrian	P321
187	Charlety, Patricia	P4
188	Chatagny, Florian	P18
189	Chatelain, Jean-Bernard	P133
190	Chen, Paul	P176
191	Chi, Chang-Koo	P180
192	Chiappinelli, Olga	P63
193	Chiarella, Carlo	P108
194	Chien, YiLi	P102
195	Choi, Sekyu	P344
196	Choi, Jin-Young	P60
197	Chu, Liya	P176
198	Chung, Kim-Sau	P54, C54, P106
199	Chusseau, Nathalie	P116, C116
200	Cipollini, Andrea	P163, C163
201	Clemens, Marius	P142
202	Clerides, Sofronis	P82, C82
203	Clymo, Alex	P48, P249
204	Cohen-Zada, Danny	P150
205	Coimbra, Nuno	P188, C188
206	Collard, Fabrice	P306
207	Collin-Dufresne, Pierre	P58
208	Combe, Julien	P234, C234
209	Commault, Jeanne	P110
210	Conrad, Christian	P170
211	Cordeiro, Yara	P346
212	Corno, Lucia	P157
213	Coroneo, Laura	P146, C146
214	Corradi, Valentina	P73, C281
215	Correia-da-Silva, Joao	P134
216	Costa Lima, Rafael	P28
217	Costain, James	P266, C266
218	Cottier, Lionel	P13
219	Coulomb, Renaud	P212
220	Couttenier, Mathieu	P382
221	Coutts, Alexander	P83
222	Currie, Janet	P282
223	D'Haultfoeuille, Xavier	P95, C95
224	Dahm, Matthias	P216
225	Dal Bianco, Chiara	P178
226	Dale-Olsen, Harald	P22
227	Dalgaard, Carl-Johan Dalgaard	P384
228	Dalkiran, Nuh Aygun	P339
229	Damgaard, Mette	P316
230	Dany, Geraldine	P343
231	Danziger, Leif	P221
232	Darolles, Serge	P203
233	Das, Kaustav	P31
234	Davezies, Laurent	P206, C206
235	Długoszek, Grzegorz	P88
236	De Angelis, Luca	P24
237	de Crombrugghe, Alain	P332, C332
238	De Fiore, Fiorella	C119, P218, C218
239	de la Garza, Adrian	P210
240	de La Rupelle, Maëlys	P80
241	De Magalhaes, Leandro	P378
242	De Nardi, Mariacristina	P110, C110
243	de Oliveira, Guilherme	P80, C80
244	de Rassenfosse, Gaetan	P217
245	De Rezende, Rafael	P175, C175, P266
246	De Rock, Bram	P303, C303
247	de Soyres, Francois	P224
248	De Vos, Ignace	P166
249	De Witte, Kristof	P86
250	Declercq, Koen	P352
251	Decreuse, Bruno	P269
252	Dehdari, Sirus	P179
253	Deimen, Inga	P181, C181
254	Dekel, Eddie	P140, C274
255	Dekker, Vincent	P367, C367
256	Delrio, Silvia	P191
257	Delventhal, Matt	P290
258	Demange, Gabrielle	P222, P338, C338
259	Demeulemeester, Sarah	P288
260	Demir, Banu	P298
261	Demont, Timothée	P111, C111
262	Denderski, Piotr	P225
263	Denti, Tommaso	P29
264	Dertwinkel-Kalt, Markus	P222, C222
265	Detemple, Jerome	P203
266	Detmers, Gunda-Alexandra	P299
267	devicienti, francesco	P184
268	Dhar, Amrita	P41
269	Di Falco, Salvatore	P350, C350
270	Dias, Daniel	P93
271	Dias de Oliveira Brito, Ricardo	P323
272	DiCecio, Riccardo	P177
273	Dickson, Alex	P6, C6
274	Dillenberger, David	P29, P129
275	Dilme, Francesc	P230, C230, P351
276	DING, SAI	P330
277	Dissanayake, Ruchith	P175
278	Dobrev, Dobrislav	P203, C203
279	Doerr, Annabelle	P120
280	Dogra, Keshav	P161, C161
281	Doko Tchatoka, Firmin	P232
282	Dolado, Juan Jose	D1, P139, C139
283	Domenech, Rafael	P143, C143
284	Dominguez Martinez, Silvia	P77
285	Dorn, David	P288, C288
286	dos Santos, Marcelo	P111
287	Dotti, Valerio	P236
288	Dovonon, Prosper	P61
289	Drugov, Mikhail	P302
290	Dube, Oeindrila	P382
291	Dubois, Pierre	P264, C264
292	Dubois, Florent	P18, C18
293	Dubois, Corinne	P220
294	Dudar, Olena	P189
295	Dumav, Martin	P230
296	Dumitrescu, Elena-Ivona	P177, C177
297	Dumitru, Ana-Maria H.	P194
298	Durrmeyer, Isis	P147
299	Dusha, Elton	P132
300	Dwarkasing, Narly	P112, C112
301	Eckert, Fabian	P10
302	Egger, Hartmut	P9
303	Einiö, Elias	P104
304	Eisenschmidt, Jens	P226
305	Ek, Andreas	P297
306	Ellwanger, Reinhard	P146
307	Endler, Johannes	P187
308	Epper, Thomas	P229, C229
309	Ergemen, Yunus Emre	P267
310	Ergun, Lerby	P250, C250
311	Erhardt, Katharina	P125
312	Espinosa, Romain	P13, C13
313	Etgeton, Stefan	P365
314	Etheridge, Ben	P172
315	Eugeni, Sara	P88
316	Everett, Mary	P79
317	Evren, Ozgur	P229
318	Exler, Florian	P173, C173, P323, C323
319	Fabre, Brice	P329
320	Facchini, Giovanni	P236, C236
321	Facchini, Gabriel	P214
322	Fackler, Thomas	P217
323	Fan, Xiaodong	P269, C269
324	Fanelli, Luca	P312
325	Fang, Hao	P238
326	Farhi, Emmanuel	P383
327	Farkas, Peter	P62
328	Fedaseyeu, Viktar	P14
329	Feger, Fabian	P6
330	Fernandes, Ana	P185
331	Fernandez, Roxana	P246, C246
332	Fernandez-Blanco, Javier	P380
333	Ferrero, Andrea	P341
334	Ferry, Marin	P183
335	Fervers, Lukas	P151
336	Fiori, Giuseppe	P90, C90
337	Fiorini, Matteo	P158
338	Flamini, Alessandro	P186, C186
339	Flemming, Jean	P169, C169
340	Flores, Carlos	P193, C193
341	Foarta, Octavia	P201
342	Foerster, Hanno	P160, C160
343	Foley-Fisher, Nathan	P36, C36
344	Fongoni, Marco	P300
345	Fosgerau, Mogens	P108
346	Frankovic, Ivan	P51
347	Fraser, Clive	P111
348	Frölich, Markus	P127, C127
349	Frick, Andreas	P15
350	Friebel, Guido	P381
351	Friedrich, Christian	P254
352	Friedrichsen, Jana	P355
353	Froemel, Maren	P183
354	Fugger, Nicolas	P291
355	Fuhrer, Lucas	P353
356	Fuster, Andreas	P86, C86
357	Gaballo, Gaetano	P87, C87, P374, C374
358	Gagliardi, Luisa	P18
359	Gagliardini, Patrick	P168
360	Galardo, Maddalena	P117
361	Galassi, Gabriela	P32, C32, P243, C243
362	Galimberti, Jaqueson	P98
363	Galuscak, Kamil	P362
364	Gamalerio, Matteo	P135
365	Garcia, Marcio	P292
366	Garcia Marin, Alvaro	P378, C378
367	Gardberg, Malin	P292
368	Garin, Julio	P153
369	Gaule, Patrick	P217
370	Gautam, Sanghmitra	P138
371	Geiger, Martin	P320
372	Geng, Yining	P356, C356
373	Gennaioli, Nicola	P71, C71
374	Georg, Co-Pierre	P228
375	Geraci, Marco Valerio	P114
376	Gerke, Rafael	P228
377	Germano, Fabrizio	P92, P192
378	Gerster, Andreas	P212
379	Gertler, Pavel	P91
380	Geyer, Johannes	P187, C187
381	Ghosh, Sugata	P297
382	Ghysels, Joris	P145
383	Giacomini, Rafaella	P281
384	Giannakopoulos, Nicholas	P44
385	Gibert Rivas, Anna	P289
386	Giesecke, Matthias	P296
387	Giesing, Yvonne	P45
388	Gille, Veronique	P245
389	Ginja, Rita	P256, C256
390	Giovannoni, Francesco	P30, C30
391	Giraudet, Gaetan	P78, C78
392	Gizatulina, Alia	P22
393	Glas, Alexander	P346
394	Gold, Robert	P92
395	Gorgens, Tue	P377, C377
396	Gorn, Alexey	P16, C16
397	Gortz, Christoph	P141
398	Goulas, Sofoklis	P5
399	Goupille-Lebret, Jonathan	P296
400	Gourio, Francois	P69
401	Grant, Nicky	P32
402	Grassi, Simona	P294, C294
403	Gravert, Jan Hendrik	P25, C25
404	Gray, Daniel	P81
405	Gräber, Nikolai	P290
406	Gröschl, Jasmin	P361
407	Greenwood-Nimmo, Matthew	P194
408	Gregor, Martin	P270
409	Grieder, Manuel	P355
410	Griffith, Rachel	C273
411	Grill, Michael	P76
412	Grillo, Edoardo	P345, C345
413	Grossmann, Volker	P309
414	Groth, Christian	P152, C152
415	Grothe, Magdalena	P177
416	Gu, Yiquan	P11
417	Gualdani, Cristina	P373
418	Guber, Raphael	P145
419	Guenette, Justin-Damien	P307
420	Guerin, Pierre	P343, C343
421	Guillot, Malka	P359
422	Gumpert, Anna	P93, C93
423	Guner, Nezih	P138, C138, P362, C362
424	Gupta, Sumedha	P90
425	Gupta, Abhimanyu	P202
426	Gurkaynak, Refet	P386
427	Gutknecht, Daniel	P370, C370
428	Haaland, Venke	P43, C43
429	Haefke, Christian	P204, C204
430	Haenni, Simon	P283
431	Hagenbach, Jeanne	P270
432	Halac, Marina	P385
433	Hamidi Sahneh, Mehdi	P375
434	Hanlon, William	P179, C179
435	Hansen, Casper	P34, C34
436	Hanspal, Tobin	P8
437	Harstad, Bard	P154, C154, P230
438	Hart, Janine	P223
439	Hatte, Sophie	P28, C28
440	Havranek, Tomas	P173
441	Hayakawa, Kazuhiko	P377
442	Haywood, Luke	P23
443	He, Xuedong	P192
444	Hedlund, Aaron	P233
445	Heiler, Phillip	P60
446	Heimisch, Alexandra	P19
447	Heinesen, Eskil	P184, C184
448	Hellman, Ziv	P196
449	Helmers, Christian	P217, C217
450	Henriksen, Espen	P27, C27
451	Hentschker, Corinna	P85
452	Hergovich, Philipp	P259
453	Hernaes, Oeystein	P324
454	Hernandez-Murillo, Ruben	P204
455	Herold, Daniel	P144
456	Hersche, Markus	P333, C333
457	Herweg, Fabian	P96, C96
458	Herz, Holger	P198
459	Hestermann, Nina	P156
460	Heyman, Fredrik	P327, C327
461	Hidalgo, Javier	P170, C170
462	Hodler, Roland	P334
463	Hoffmann, Timo	P349
464	Hoffmann, Bridget	P38, P378
465	Hofmann, Boris	P226
466	Holden, Tom	P98
467	Holly, Alberto	P272, C272
468	Holtsmark, Katinka	P181
469	Holzmann, Hajo	P376
470	Homrighausen, Pia	P160
471	Honarvar, Iman	P357
472	Hong, Seung Hyun	P373
473	Hopkins, Ed	P20, C20, C280
474	Horie, Mayumi	P229
475	Horvath, Michal	P47
476	Hoshino, Tadao	P61
477	Hristov, Nikolay	P218
478	Hrung, Warren	P210
479	Hu, Audrey	P96
480	Hu, Bo	P311
481	Huber, Martin	P95
482	Huber, Stefanie	P252
483	Hubert, Paul	P26
484	Huffman, Gregory	P161
485	Hugonnier, Julien	P231
486	Hur, Jung	P327
487	Hurkens, Sjaak	P164, C164
488	Hwang, Jungbin	P24
489	Iacono, Roberto	P247
490	Ichino, Andrea	P145, C145
491	ielpo, Florian	P237
492	Ilzetzki, Ethan	P260, P309, C309
493	Imbert, Clément	P213, C213
494	Imrohoroglu, Selahattin	P45
495	Imura, Yuko	P190
496	Irlacher, Michael	P190
497	Irmen, Andreas	P143
498	Irsova, Zuzana	P298
499	Ispano, Alessandro	P30
500	Issler, João Victor	P304
501	Istrefi, Klodiana	P191
502	Izmalkov, Sergei	P197
503	Jacob, Arun	P150, C150
504	Jank, Stephan	P36
505	Jäger, Philipp	P368, C368
506	Jensen, Peter	P85
507	Jeong, Seungwon (Eugene)	P227
508	Jermann, Urban	P69, C69
509	Jhang, Hogyu	P239
510	Jo, Ara	P122
511	John, Anett	P20
512	Johnsen, Julian	P185
513	Jondeau, Eric	P238, C238
514	Jung, Alexander	P117
515	Jungherr, Joachim	P141, C141, P201
516	Kabukcuoglu, Ayse	P130
517	Kalantzis, Yannick	P121, C121
518	Kampfen, Fabrice	P293
519	Karabarbounis, Marios	P84
520	Karanasos, Menelaos	P56, C56
521	Karle, Heiko	P216, P310
522	Kaszab, Lorant	P364, C364
523	Kaufmann, Christoph	P224
524	Kaufmann, Daniel	P91
525	Kaufmann, Sylvia	P101, C101
526	Kawamura, Kohei	P107
527	Kölle, Felix	P349, C349
528	Kösler, Markus	P174
529	Küchlin, Eva-Maria	P64, C64
530	Kelly, Elaine	P214, C214
531	Kelsey, David	P261
532	Kempf, Hubert	P119
533	Kermani, Amir	P309
534	Kettemann, Andreas	P335
535	Khadjavi, Menusch	P350
536	Khalil, Makram	P27
537	Khrapov, Stanislav	P64, P177
538	Khromenkova, Daria	P31
539	Kiedaisch, Christian	P15, C15
540	Kim, Jin Yeub	P149, C149
541	Kim, Taejin	P308
542	Kimasa, Bihemo	P35
543	Kittsteiner, Thomas	P180
544	Klößner, Stefan	P205
545	Kleen, Onno	P68
546	Klein, Thilo	P244
547	Klimenka, Filip	P139
548	Knell, Markus	P329, C329
549	Knyazev, Dmitriy	P15, P227
550	Kobayashi, Keiichiro	P25
551	Koch, Christoffer	P228, C228
552	Kockesen, Levent	P171, C171
553	Koenig, Tobias	P92
554	Koenig, Christoph	P14, C14
555	Koenig, Michel	P288
556	Koeniger, Winfried	P323
557	Koetter, Michael	P226, C226
558	Kofoed, Michael	P195
559	Koijen, Ralph	P71
560	Kolasa, Marcin	P233
561	Kolly, Jeremy	P97
562	Kolotilin, Anton	P136
563	Kondor, Peter	P313, C313
564	Kondor, Peter	P71
565	Kools, Lieke	P187
566	Koop, Gary	P97
567	Koren, Miklós	D1
568	Korinek, Anton	P383
569	Kormilitsina, Anna	P340
570	Kornienko, Tatiana	P107
571	Korpeoglu, Cigdem Gizem	P310
572	Kosar, Gizem	P32
573	Kosonen, Tuomas	P49
574	Kostka, Thomas	P7
575	Koszegi, Botond	P74
576	Kotakorpi, Kaisa	P13
577	Kourtellos, Andros	P61, C61, P215
578	Koutmeridis, Theodore	P19, C19
579	Krause, Melanie	P10, C10
580	Krüger, Fabian	P97
581	Krehlik, Tomas	P174
582	Kreiser, Swetlana	P240, C240
583	Krenz, Johanna	P3
584	Krippner, Leo	P328, C328
585	Krishnakumar, Jaya	P207
586	Krumer, Alex	P284
587	Kudlyak, Marianna	P225, C225
588	Kultti, Klaus	P15
589	Kumru, Cagri	P374
590	Kung, Howard	P124, C124
591	Kung, James	P384
592	Kunz, Johannes	P319
593	Kurmann, Andre	P219, C219
594	Kurtzman, Robert	P337, C337
595	Kushnir, Alexey	P134, C134
596	Kyriakopoulou, Dimitra	P56
597	Kyriazidou, Ekaterini	P166, C166
598	Kyyrä, Tomi	P160
599	L'Hour, Jérémy	P193
600	La Ferrara, Eliana	P277
601	La'O, Jennifer	P278
602	Lach, Saul	P147, C147
603	Lai, Tat-kei	P58, C58
604	Lalé, Etienne	P90, P380, C380
605	Lalive, Rafael	P44, C44
606	Lambertini, Luisa	P289, C289
607	Lampaert, Kevin	P357
608	Lamy, Laurent	P96
609	Landaud, Fanny	P195
610	Lane, Philipp	D75
611	Larch, Mario	P10
612	Laurentsyeva, Nadzeya	P363, C363
613	Laureys, Lien	P253
614	Lavergne, Pascal	P202, C202
615	Lazarova, Emiliya	P287
616	Lazzaroni, Sara	P260, C260
617	López-Pérez, Víctor	P177
618	Lüdering, Jochen	P184
619	LE YAOUANQ, Yves	P54
620	Lechthaler, Wolfgang	P190
621	Lee, Junghoon	P100
622	Lee, Sang Yoon (Tim)	P293, C293
623	Legge, Stefan	P290
624	Legrand, Nicolas	P178
625	Lenel, Friederike	P83, C83
626	Lenza, Michele	P191, C191
627	Lepage-Saucier, Nicolas	P94
628	Leturcq, Marion	P44
629	Levell, Peter	P33, C33
630	Levintal, Oren	P98
631	Lewbel, Arthur	P206
632	Leymarie, Jérémy	P163
633	Li, Jingchao	P133
634	Li, Wei	P79
635	Li, Chen	P9
636	Li, Bin Grace	P46, C46
637	Li, Mengling	P311
638	Li, Shengyu	P264
639	Li, Wenli	P233
640	Liberini, Federica	P189
641	Libert, Thibault	P337
642	Lieli, Robert	P307, C307
643	Lifshitz, Osnat	P172
644	Lingens, Jörg	P19
645	Link, Sebastian	P320, C320
646	Liu, Lucy Qian	P285, C285
647	Liu, Yulin	P364
648	Liu, Nianqing	P206
649	Liu, Shuo	P291
650	Liu, Ting	P339
651	Liu, Chu-An	P377
652	Liu, Ruixuan	P60, C60
653	Loertscher, Simon	P164, P180
654	Lomys, Niccolo	P313
655	Lopes da Fonseca, Mariana	P123
656	Lopez, Pierlauro	P51
657	Loria, Francesca	P254, C254, P299
658	Lozej, Matija	P183
659	Lu, Anna	P147
660	Luetticke, Ralph	P259
661	Luger, Richard	P238
662	Lundberg, Clark	P131
663	Luoto, Jani	P57
664	Lychagin, Sergey	P5
665	Maas, Daniel	P379, C379
666	Macera, Rosario	P77, C77
667	Machado, Matilde	P322
668	Machado, Cecilia	P195, C195, P325
669	Madeira, Carlos	P266
670	Magnolfi, Lorenzo	P373, C373
671	Maier, Johannes	P109
672	Malamud, Semyon	P313
673	Malde, Bansi	P317, C317
674	Malik, Samreen	P2
675	Maltz, Amnon	P162
676	Mandler, Martin	P26, P240
677	Maneesoonthorn, Worapree	P68
678	Manner, Hans	P307
679	Manova, Kalina	P70, C70, P221
680	Mantovan, Noemi	P185
681	Manzano, Carolina	P128, C128
682	Manzini, Paola	P74
683	March, Christoph	P107, C107
684	Marchenko, Maria	P5
685	Marcus, Jan	P211
686	Marimon, Ramon	P51, C51
687	Mariotti, Thomas	P385
688	Markazi Moghadam, Hamed	P174
689	Marra, Marleen	P246
690	Martin, Simon	P216, C216
691	Martinez, Isabel	P333
692	Martins, Luis Filipe	P21
693	Martins-da-Rocha, V. Filipe	P102
694	Marvao, Catarina	P222
695	Marx, Leslie	P263, P318
696	Mateos-Planas, Xavier	P332
697	Matsui, Jun	P174
698	Matsushima, Hitoshi	P103, C103
699	Matthys, Felix	P124
700	Mattozzi, Andrea	P63
701	Maurer, Stephan	P179
702	Mavroeidi, Eleonora	P121
703	Mayoral, Laura	P260
704	Mayr, Lukas	P8
705	Mazelis, Falk	P240, P275
706	Mazur, Karol	P331
707	Ménager, Lucie	P55, C55
708	Müller, Dagmar	P184
709	McAdam, Peter	P42
710	McCabe, Brendan	P137
711	McCracken, Michael	P235, C235, P281
712	McLeay, Michael	P186
713	McLennan, Andy	P196
714	Mehrotra, Neil	P383, C383
715	Mehrotra, Rahul	P83
716	Meier, Mario	P335, C335
717	Meier, Matthias	P375
718	Meinen, Philipp	P52, C52
719	Meirowitz, Adam	C200
720	Meitz, Mika	P57
721	Meling, Tom	P250
722	Mengel, Friederike	P150
723	Menicucci, Domenico	P11
724	Mercier, Marion	P334, C334
725	Mergele, Lukas	P258
726	Merkurieva, Irina	P225
727	Merola, Rossana	P220
728	Metiu, Norbert	P295
729	Metzger, Lars	P103
730	Metzing, Maria	P116
731	Michau, Jean-Baptiste	P121
732	Micheli, Martin	P219
733	Mierau, Jochen	P116
734	Miettinen, Topi	P11, C11
735	Mihm, Maximilian	P129
736	Mill, Wladislaw	P241, C241
737	Mitman, Kurt	P309
738	Mitra, Anirban	P345
739	Mittag, Nikolas	P205
740	Miura, Shintaro	P30
741	Mocan, Naci	P39
742	Mocking, Remco	P33
743	Moench, Emanuel	P130
744	Moessner, Richhild	P295, C295
745	Molteni, Francesco	P188
746	Monfort, Alain	P340, C340
747	Monnet, Cyril	P305, C305
748	Montez, Joao	P291
749	Montiel Olea, Jose	P375, C375
750	Morana, Claudio	P376, C376
751	Morchio, Iacopo	P169
752	Morelli, Massimo	P200
753	Moreno, Santiago	P230
754	Moreno de Barreda, Ines	P270, C270
755	Moretti, Laura	P46
756	Moriconi, Simone	P297
757	Moscoso Boedo, Hernan	P379
758	Moser, Christian	P296, C296
759	Mouabbi, Sarah	P12
760	Mouganie, Pierre	P211, C211
761	Mourifie, Ismael	P113, P193
762	Moxnes, Andreas	P70
763	Muellbauer, John	P252, C252
764	Mueller, Andreas	P16
765	Mueller, Tobias	P294
766	Mukherjee, Rahul	P286, C286
767	Mukherjee, Abhik	P182
768	Muller, Christophe	P243
769	Munyo, Ignacio	P303
770	Murao, Tetsushi	P331
771	Murooka, Takeshi	P156, C156
772	Mylovanov, Tymofiy	P369
773	Mysliwski, Mateusz	P354
774	Nagaoka, Sadao	P288
775	Naguib, Costanza	P68
776	Nakagawa, Ryuichi	P87
777	Nakaguma, Marcos	P167
778	Narciso, Gaia	P45, C45
779	Nasir, Harun	P328
780	Natoli, Filippo	P292
781	Nava, Francesco	P197
782	Nax, Heinrich	P196
783	Nax, Heinrich	P371, C371
784	Nöldeke, Georg	P63, C63
785	Neary, Peter	P221, C221, P263
786	Nedoncelle, Clément	P52
787	Neugart, Michael	P16
788	Neugebauer, Katja	P285
789	Neuhierl, Andreas	P146
790	Ng, Serena	P73
791	Nguyen, Tuan	P363
792	Nibbering, Didier	P343
793	Niedermayer, Andras	P354, C354
794	Niedermayer, Kilian	P256
795	Nikolov, Boris	P286
796	Nikolowa, Radoslawa	P369
797	Nimczik, Jan Sebastian	P257, C257
798	Noe, Thomas	P339, C339
799	Nordström, Jonas	P39, C39
800	Nordvik, Frode Martin	P27
801	Nuguer, Victoria	P275, C275
802	NYAWA WOMO, Serge Luther	P347, C347
803	o'higgins, niall	P283, C283
804	O'Toole, Conor M	P186
805	Obergruber, Natalie	P205
806	Ochoa, Marcelo	P239, C239
807	Ochsner, Christian	P294
808	Odermatt, Reto	P39
809	Oduncu, Arif	P275
810	Oikawa, Koki	P37
811	Olarreaga, Marcelo	P207
812	Olsson, Martin	P248
813	Olsson, Ola	P384, C384
814	Ongena, Steven	P79
815	Oosterveen, Matthijs	P5, C5
816	Opschoor, Anne	P62, C62
817	Origo, Federica	P185
818	Ortega, Eva	P130, C130
819	Ossola, Elisa	P139
820	Ostenstad, Gry	P361
821	Oto-Peralias, Daniel	P80
822	Otsu, Taisuke	P202
823	Ott, Marion	P227, C227
824	Oyekola, Olayinka	P27
825	Ozhan, Galip	P3
826	Ozkan, Serdar	P133, C133
827	Paczos, Marta	P118
828	Pagnotta, Emiliano	P231, P231, P231, P231
829	Pagnozzi, Marco	P105
830	Pakel, Cavit	P271
831	Palma, Nuno	P91
832	Pappa, Evi	P341, C341
833	Park, Kyoung Sun	P353
834	Parkhomenko, Andrii	P272
835	Patnam, Manasa	P268, C268
836	Paukkeri, Tuuli	P215
837	Paul, Alexander	P358
838	Pavoni, Nicola	P55, C385
839	Peacey, Mike	P81
840	Pederzoli, Paola	P203
841	Pegoraro, Fulvio	P194
842	Pehlivan, Ayse	P264
843	Pelletier, Denis	P237, C237
844	Penasse, Julien	P21
845	Penczynski, Stefan	P107
846	Peng, Baochun	P329
847	Pernaudet, Julie	P322
848	Persson, Torsten	P277
849	Petropoulos, Georgios	P37, C37
850	Pettenuzzo, Davide	P301
851	Pfister, Curdin	P81
852	Pham-Dao, Lien	P259
853	Piatek, Rémi	P301
854	Picariello, Luca	P144, C144
855	Pickering, Andrew	P201, P366, C366
856	Piffer, Michele	P191
857	Pilny, Adam	P214
858	Pinto, Cristine	P370
859	Pizzinelli, Carlo	P169
860	Plantin, Guillaume	P279
861	Podstawski, Maximilian	P175
862	Poelhekke, Steven	P34
863	Pohlan, Laura	P151
864	Polanski, Arnold	P181
865	Pollrich, Martin	P302
866	Pomeranz, Dina	P189
867	Ponthiere, Gregory	P356
868	Pope, Thomas	P50
869	Popov, Sergey	P284
870	Porter, Robert	C140
871	Pradelski, Bary	P371
872	Pröhl, Elisabeth	P98, C98
873	Pritsker, Matthew	P163
874	Proebsting, Christian	P224
875	Puaschunder, Julia	P209
876	Puch, Luis	P337
877	Pytlikova, Mariola	P236
878	Qi, Shaofang	P162
879	Quadrini, Vincenzo	P69
880	Quast, Bastiaan	P34
881	Queralto, Albert	P249, C249
882	Quigley, Daniel	P308, C308
883	Quintin, Erwan	P102
884	Rabaté, Simon	P187
885	Rablen, Matthew	P144
886	raciborski, rafal	P328
887	Raczko, Marek	P124
888	Raes, Louis	P36
889	Ragot, Xavier	P48, C48
890	Rahi, Rohit	P105
891	Ramsden, Alma	P187
892	Ranehill, Eva	P77
893	Rannenberg, Ansgar	P220, C220
894	Rasul, Imran	P381
895	Rauh, Christopher	P321, C321
896	Rausch, Sebastian	P287
897	Ravazzolo, Francesco	P97, C97
898	Ravetti, Chiara	P247, C247
899	Ravid, Doron	P29
900	Ray, Debraj	P66
901	Redlicki, Jakub	P123
902	Rehbein, Oliver	P182, C182
903	Reich, Gregor	P108
904	Reijnders, Laurie	P293
905	Reinold, Kate	P110
906	Reischmann, Andreas	P22, C22
907	RENNE, Jean-Paul	P312
908	Renner, Laura	P223
909	Repullo, Rafael	P233, C233
910	Reshef, Ariell	P359, C359
911	Rickert, Dennis	P246
912	Rilstone, Paul	P232
913	Rincon, Hernan	P148
914	Ristiniemi, Annukka	P159, C159
915	Roberti, Paolo	P28
916	Roeder, Kerstin	P40
917	Roehe, Oke	P191
918	Roesler, Anne-Katrin	P31
919	Roettger, Joost	P113, P201
920	Roevekamp, Ingmar	P7
921	Rohner, Dominic	P200, P334
922	Rojcek, Jakub	P231, C231
923	Roland, Michel	P222
924	Roldan, Pau	P68
925	Roling, Christoph	P357, C357
926	Roller, Marcus	P333
927	Romero-Medina, Antonio	P311, C311
928	Ropponen, Olli	P189
929	Rose, Michael	P293
930	Rosenbaum, Philip	P185, C185
931	Rossi, Barbara	C282
932	Rostam-Afschar, Davud	P325
933	Rothfelder, Mario Philipp	P232, C232
934	Roudaut, Gwenael	P286
935	Roulleau-Pasdeloup, Jordan	P84, C84
936	Roussellet, Guillaume	P101
937	Rubínová, Stela	P9, C9
938	Rubio, Margarita	P119
939	Rudiger, Jesper	P351
940	Rueth, Sebastian	P295
941	Rutkowski, Felix	P186
942	Rydzek, Benedikt	P189, C189
943	Sablina, Maria	P241
944	Sadaba, Barbara	P238
945	Sadun, Raffaella	C381
946	Sahari, Anna	P212, C212
947	Salamanca, Nicolas	P356
948	Samano, Mario	P82
949	Santos Monteiro, Paulo	P317
950	Santos-Pinto, Luis	P192, C192
951	Saponara, Nick	P261, C261
952	Saporta, Itay	P381
953	Sasaki, Yuya	P127
954	Sato, Kiyotaka	P148
955	Sauré, Philip	P148, C148
956	Saussay, Aurélien	P212
957	Savignac, Frédérique	P33
958	Savolainen, Riikka	P14
959	Schaz, Philipp	P285
960	Schempp, Paul	P208
961	Schenone, Pablo	P165, C165
962	Schildberg-Hoerisch, Hannah	P283
963	Schilling, Linda	P308
964	Schippers, Anouk	P126, C126
965	Schlafmann, Kathrin	P20
966	Schlag, Karl	P35
967	Schmelz, Katrin	P355, C355
968	Schmitt, Stefanie	P351, C351
969	Schmitz, Tom	P342, C342
970	Schmutzler, Armin	P198, C198
971	Schneider, Ulrike	P314
972	Schneider, Johannes	P302
973	Schober, Dominik	P367
974	Schottmueller, Christoph	P149, P369
975	Schreger, Jesse	P279
976	Schreiner, Ragnhild Camilla	P322, C322
977	Schudy, Simeon	P6
978	Schueler, Yves Stephan	P2, C2
979	Schuler, Tobias	P220
980	Schulz, Bastian	P344
981	Schumacher, Malte	P175
982	Schumann, Martin	P166
983	Schwab, Jakob	P327
984	Schweighofer-Kodritsch, Sebastian	P53
985	Schwerin, Hagen	P38, C38
986	Seele, Stefanie	P325, C325
987	Selcuk, Cemil	P128
988	Senay, Ozge	P224, C224
989	Senga, Tatsuro	P87, P342
990	Senn, Julien	P77
991	Sentana, Enrique	C73, P168, C168
992	Serafinelli, Michel	P268
993	Serena, Marco	P180
994	Serfes, Konstantinos	P104
995	Serizawa, Shigehiro	P65
996	Serrano-Padial, Ricardo	P308
997	Severgnini, Battista	P213
998	Sgroi, Daniel	P152
999	Shadmehr, Mehdi	P167
1000	Shaw, Jonathan	P257
1001	Sheard, Nicholas	P18
1002	Sheedy, Kevin	P200, C201
1003	Sheveleva, Lena	P93
1004	Shin, Yonghceol	P315, C315
1005	Shioji, Etsuro	P226
1006	Shupe, Cortnie	P49, C49
1007	Siedlarek, Jan-Peter	P112
1008	Siegenthaler, Michael	P363
1009	Siemroth, Christoph	P305
1010	Siena, Daniele	P265, C265
1011	Siikanen, Markku	P155, C155
1012	Simonelli, Saverio	P188
1013	SIN, Chor-yiu (CY)	P62
1014	Singh, Nirvikar	P379
1015	Sirchenko, Andrei	P299
1016	Skans, Oskar	P245
1017	Skreta, Vasiliki	P29, C29, P106, C106
1018	Smets, Frank	C75
1019	Soares, Carla	P249
1020	Sobbrio, Francesco	P28
1021	Sobel, Joel	C74, P136, C136
1022	Sobolev, Anton	P35, C35
1023	Soetevent, Adriaan	P197, C197
1024	Sofianos, Andis	P209, C209
1025	Sokullu, Senay	P314, C314
1026	Solleder, Olga	P125, C125
1027	Sonin, Konstantin	P345
1028	Sorensen, Bent	P368
1029	Sovinsky, Michelle	P276, C276
1030	Spantig, Lisa	P126
1031	Speck, Christian	P295
1032	Spiess, Jann	P95
1033	Srivastava, Vatsalya	P181
1034	St-Amour, Pascal	P336
1035	Staal, Klaas	P92, C92
1036	Stacescu, Bogdan	P208
1037	Stadelmann, Marcel	P6
1038	Staszewska-Bystrova, Anna	P312, C312
1039	Steiner, Andreas	P118, C118
1040	Steiner, Elizabeth	P219
1041	Stella, Andrea	P215, C215
1042	Stentoft, Lars	P271
1043	Stepanov, Sergey	P149
1044	Sterzel, André	P188
1045	Stitzing, Robin	P287
1046	Stoerk, Thomas	P287, C287
1047	Stoltenberg, Christian A.	P360
1048	Storesletten, Kjetil	P42, C42
1049	Stowasser, Till	P241
1050	Stoyanov, Andrey	P125
1051	Stoye, Joerg	P57, C57
1052	Strack, Philipp	P198
1053	Strømland, Eirik	P209
1054	Strifler, Matthias	P300
1055	Strittmatter, Anthony	P205, C205
1056	Strobl, Günter	P4, C4
1057	Stutzer, Alois	P255, C255
1058	Suen, Richard M. H.	P25
1059	Sulka, Tomasz	P296
1060	Sun, Yiqiao	P12
1061	Syed, Iqbal	P64
1062	Syverson, Chad	P276
1063	Szalay, Dezso	P136
1064	Szech, Nora	P96, P198, P283
1065	Szydlowski, Arkadiusz	P206
1066	Tabasso, Domenico	P300
1067	Tabellini, Guido	D75
1068	Takahashi, Hidenori	P155
1069	Takats, Elod	P79
1070	Tamagni, Federico	P37
1071	Tambakis, Demosthenes	P115
1072	Tamoni, Andrea	P346, C346
1073	Tarasov, Alexander	P315
1074	Tasci, Murat	P258, C258
1075	Taufemback, Cleiton	P235
1076	Taylor, Karl	P94
1077	Taylor, Robert	P24
1078	Tchuente, Guy	P314
1079	Teignier, Marc	P8, C8
1080	Telalagic, Selma	P23, P40, C40
1081	telg, sean	P307
1082	Temzelides, Ted	P59
1083	Tergiman, Chloe	P53, C53, P154
1084	Terrier, Camille	P234
1085	Tesar, Linda	P289
1086	Thanassoulis, John	P199
1087	Thimme, Julian	P353, C353
1088	Thoenig, Mathias	C382
1089	Thorsrud, Leif Anders	P173
1090	Tille, Cedric	C207, P210, C210
1091	Tinang, Jules	P239
1092	Tischbirek, Andreas	P159
1093	Tolan, Songül	P178, C178
1094	Tonini, Sara	P209
1095	Toth, Russell	P213, P370
1096	Trapeznikova, Ija	P272
1097	Traum, Nora	P306, C306
1098	Trew, Alex	P59
1099	Trindade, Andre	P330
1100	Tristani, Oreste	P101, C259
1101	Troeger, Thomas	P106
1102	Trojani, Fabio	P237
1103	Troster, Victor	P170
1104	Troumpounis, Orestis	P135
1105	Troya-Martinez, Marta	P262, C262
1106	Tuncel, Tuba	P85, C85
1107	Tuomala, Juha	P365
1108	Tur-Prats, Ana	P248, C248
1109	Turcu, Camelia	P10
1110	Turner, Lesley	P195
1111	Tymula, Agnieszka	P109, C109, P310
1112	Tyson, Christopher	P229
1113	Ueda, Kozo	P374
1114	Uhrin, Gábor	P183, P312
1115	Ungeheuer, Michael	P326, P326
1116	Ura, Takuya	P193
1117	Ushchev, Philipp	P165
1118	Utar, Hale	P17
1119	Vaccaro, Giannina	P251
1120	Vacha, Lukas	P275
1121	Valchev, Rosen	P305
1122	Valdes, Gonzalo	P158
1123	Valls Pereira, Pedro	P21
1124	Van Belle, Eva	P324
1125	van der Weele, Joel	P156
1126	van Dijk, Herman	P301, C301
1127	Van Ewijk, Reyn	P358
1128	van Norden, Simon	P21, C21, P299, C299
1129	van Veelen, Matthijs	P196, C196
1130	van Wijnbergen, Sweder	P208, C208
1131	Vandewalle, Lore	P244
1132	Vardoulakis, Alexandros	P76
1133	Vasama, Suvi	P55
1134	Vasicek, Borek	P41, C41
1135	Vassilatos, Vanghelis	P2, P306
1136	Vázquez, Jesús	P100
1137	Velasco, Carlos	P267, C267
1138	Venkatesh, Raghul	P255
1139	Venkateswaran, Venky	P278, C278
1140	Verboven, Frank	P276
1141	Veselov, Dmitriy	P143
1142	Viarengo, Martina	P122
1143	Vicente, Ricardo	P332
1144	Vicondoa, Alejandro	P265
1145	Vigier, Adrien	P132, P171
1146	Vlachos, Stephanos	P157, C157
1147	Vladimirov, Vladimir	P4
1148	Wagner, Natascha	P352, C352
1149	Wagner, Martin	P267
1150	Wakamori, Naoki	P82
1151	Walther, Ansgar	P132, C132
1152	Wang, Haomin	P256
1153	Wang, Zhu	P104, C104, P216
1154	Wang, Xuexin	P202
1155	Wang, Chaojun	P165, P250
1156	Wang, Cheng	P338
1157	Wang, DANDAN	P232
1158	Ward, Felix	P179
1159	Wasser, Cédric	P318, C318
1160	Watson, Mark	P274, C386
1161	Weber, Michael	P91, C91, P304
1162	Weber, Thomas	P181
1163	Weber, Andrea	P365, C365
1164	Wegner, Nora	P103
1165	Werner, Katharina	P319, C319
1166	Westermark, Andreas	P331, C331
1167	Westling, Tatu	P184
1168	Wiederholt, Mirko	P278
1169	Wilemme, Guillaume	P178
1170	Wilhelm, Matthias	P90
1171	Wilms, Ole	P64
1172	Wilson, Chris	P11
1173	Winant, Pablo	P88, C88
1174	Winkler, Erwin	P361, C361
1175	Winter, Christoph	P218
1176	Witajewski-Baltvilks, Jan	P297, C297
1177	Wittneben, Christian	P89
1178	Wolf, Christoph	P31, C31
1179	Wolter, Stefan	P319
1180	Wolton, Stephane	P167, C167, P255
1181	Wu, Binzhen	P336
1182	Xu, Guo	P284
1183	Xu, Qi	P7
1184	Yamashita, Takuro	P164
1185	Yang, Youzhi	P262
1186	Yariv, Leeat	P280
1187	Yasuda, Yosuke	P103
1188	Yavuzoglu, Berk	P138
1189	Yilmaz, Kamil	P194, C194
1190	Yoo, Donghoon	P100, P360, C360
1191	Yoo, Hong Il	P376
1192	Yoshimoto, Hisayuki	P104
1193	Yotov, Yoto	P315
1194	Ytsma, Erina	P19, P344, C344
1195	Yu, Yuejuan	P182
1196	Yurdagul, Emircan	P290, C290
1197	Zahiri, Sepideh	P26
1198	Zankiewicz, Christian	P129, C129
1199	Zapal, Jan	P14, P262
1200	Zapechelnyuk, Andriy	P261
1201	Zegners, Dainis	P82
1202	Zeke, David	P161
1203	Zeng, Jing	P4, P338
1204	Zenker, Juliane	P243
1205	Zer, Ilknur	P41
1206	Zhang, Shengxing	P313
1207	Zhang, Xin	P228
1208	Zhang, Sihong	P310, C310
1209	Zhang, Ally Quan	P68
1210	Zhao, Jake	P372
1211	Zhao, Xiaolu	P347
1212	Zheng, Yu	P42
1213	Zhou, Jin	P122, C122
1214	Zhou, Yu	P65
1215	Zi, Yuan	P17, C17
1216	Ziegler, Lennart	P13
1217	Zilibotti, Fabrizio	P273, C348
1218	Zizza, Roberta	P204
1219	Zouain Pedroni, Marcelo	P48
1220	Zryumov, Pavel	P171
1221	Zylberberg, Yanos	P115, C115, P380
1222	Zymek, Robert	P298, C298
"""

# Step 3: Parse names from that block
all_website_names = set()
for line in participant_text.strip().splitlines():
    match = re.match(r'\d+\s+([\w\-\'. ]+),\s+([\w\-\'. ]+)', line)
    if match:
        last = match.group(1).strip()
        first = match.group(2).strip()
        full_name = f"{first} {last}"
        all_website_names.add(full_name)

# Step 4: Compare
missing = all_website_names - extracted_presenters

# Step 5: Output
print(f"✅ Total from website: {len(all_website_names)}")
print(f"🟨 Missing from CSV: {len(missing)}\n")
for name in sorted(missing):
    print(name)

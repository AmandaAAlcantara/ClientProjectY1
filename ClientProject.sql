DROP TABLE if EXISTS Checkpoints;
CREATE TABLE if not EXISTS "Checkpoints" ( "ID" INTEGER not NULL PRIMARY KEY AUTOINCREMENT, "Name" TEXT, "Picture" TEXT, "Facts" TEXT, "Contacts" TEXT);

INSERT INTO Checkpoints ("ID", "Name", "Picture","Facts") VALUES ("1", "Redwick", "/static/LandmarkImg/Redwick.jpg", "Redwick is the best-preserved medieval village
on the Gwent Levels. The village probably
originated late in the eleventh century; its
layout has hardly changed since.
The church, St Thomas the Apostle, is well
worth a visit. Among its unique features, the
church has medieval stone carvings, a full
immersion baptistery and its font originates
from the 13th Century. Two of the six bells
in the central tower date from the pre-reformation period and are thought to be
some of the oldest working church bells in
the country.");

INSERT INTO Checkpoints ("ID", "Name", "Picture","Facts") VALUES ("2", "Whitson","/static/LandmarkImg/Whitson.jpg", "The houses and farmsteads in Whitson are set
back from the road in long strips of pasture.
It reflects a medieval ‘cope’ land allocation
pattern. This fascinating landscape was
planned out between the 11th and 13th
century, possibly by the monks at Goldcliff.
“Monksditch” also known as “Goldcliff Pill”
passes through the village on its way to the sea.
Monkditch carries water from an upland stream
to the coast, preventing the fresh water from
flooding the levels. It was first documented in
the 13th Century and probably constructed by
the monks at Goldcliff. ");

INSERT INTO Checkpoints ("ID", "Name", "Picture","Facts","Contacts") VALUES ("3", "Goldcliff Sea Wall
and Priory","/static/LandmarkImg/GoldcliffSeaWall.jpg", "Giraldus Cambrensis, who toured Wales in 1188,
described Gouldclyffe in Latin as ‘glittering with
a wonderful brightness’.
Goldcliff was named after a limestone cliff,
about 60 feet high, that once rose over a
great bed of yellow mica that had a glittering
appearance in sunshine, especially to ships
passing in the Bristol Channel.
Goldcliff was an island until the sea wall was
built. In 1113AD the Norman Lord of Caerleon
granted the Benedictines a priory which was
built on the island of Goldcliff. The monks were
also given the surrounding land to farm though
they had to reclaim it from the sea – continuing
the work of the Romans.
Goldcliff has long been associated with the tidal
fishing of salmon, which may well have had its
origins with the Priory or even in Roman times.","Natural Resources Wales - 01633 292 982");

INSERT INTO Checkpoints ("ID", "Name", "Picture","Facts") VALUES ("4","The Wetlands Centre", "/static/LandmarkImg/TheWetLandsCentre.jpg", "The Wetlands Centre is nestled among reeds
and pools to make it look as if it’s floating.
The centre was opened in 2008 and is now
managed by the RSPB. It houses a shop, café,
an education room and conference facilities to
provide activities and events as well as a place
for visitors to relax. Guided walks around the
Reserve can be arranged from here.");



CREATE TABLE if not EXISTS "Enquiries" ( "Text" TEXT, "Email" TEXT);
INSERT INTO Enquiries ("Text", "Email") VALUES ("Text", "Email");


DROP TABLE if EXISTS Routes;
CREATE TABLE if not EXISTS "Routes" ( "Picture" TEXT, "Name" TEXT, "Info" TEXT);
INSERT INTO Routes ("Picture", "Name", "Info") VALUES ("/static/Routes/TredegarHouse.jpg", "Dyffryn Gardens and Tredegar House", "Free entry perfect for an afternoon walk");
INSERT INTO Routes ("Picture", "Name", "Info") VALUES ("/static/Routes/Coalstal.jpg", "Newport Coastal Paths", "Free entry perfect for an afternoon walk");
INSERT INTO Routes ("Picture", "Name", "Info") VALUES ("/static/Routes/RomanFortress.jpeg", "Caerleon Roman Fortress and Baths", "Free entry perfect for an afternoon walk");
INSERT INTO Routes ("Picture", "Name", "Info") VALUES ("/static/Routes/BelleVue.jpg", "Belle Vue Park Walk", "Free entry perfect for an afternoon walk");

DROP TABLE if EXISTS RoutesC;
CREATE TABLE if not EXISTS "RoutesC" ( "Picture" TEXT, "Name" TEXT, "Info" TEXT);
INSERT INTO RoutesC ("Picture", "Name", "Info") VALUES ("/static/Routes/RiverUsk.jpg", "River Usk Path", "Free entry perfect for an afternoon walk");
INSERT INTO RoutesC ("Picture", "Name", "Info") VALUES ("/static/Routes/Arcades.jpg", "Arcades, Cafes and Stores", "Free entry perfect for an afternoon walk");
INSERT INTO RoutesC ("Picture", "Name", "Info") VALUES ("/static/Routes/BoatClub.jpeg", "Newport Boat Club", "Free entry perfect for an afternoon walk");
INSERT INTO RoutesC ("Picture", "Name", "Info") VALUES ("/static/Routes/CityCentre.jpg", "City Centre Walk", "Free entry perfect for an afternoon walk");


DROP TABLE if EXISTS Commentssubmission;
CREATE TABLE if not EXISTS "Commentssubmission" ("NameOfRoute" TEXT, "NameOfLocation" TEXT, "Comment" TEXT);
INSERT INTO Commentssubmission ("NameOfRoute", "NameOfLocation", "Comment") VALUES ("?" , "?" , "?");


DROP TABLE if EXISTS DisabilityF;
CREATE TABLE if not EXISTS "DisabilityF" ( "Picture" TEXT, "Name" TEXT, "Info" TEXT);
INSERT INTO DisabilityF ("Picture", "Name", "Info") VALUES ("/static/Routes/IndorMarket.jpg", "City Tour", "Acessible and has amazing stops for lunch along the way");


DROP TABLE if EXISTS Events;
CREATE TABLE if not EXISTS "Events" ( "Date" TEXT, "Name" TEXT, "Info" TEXT, "Time" INTEGER);
INSERT INTO Events ("Date", "Name", "Info", "Time") VALUES ("18th December", "Festive 5k", "Newport Council envites you to join us as we vist all of Newports historical sites", "10:00");
INSERT INTO Events ("Date", "Name", "Info", "Time") VALUES ("26th December", "Boxing Day Path", "Join us on the 26th as we explore newport coasts","10:45 ");
INSERT INTO Events ("Date", "Name", "Info", "Time") VALUES ("8th January", "Wildlife Protection Path", "For all the wildlife lovers!", "11:00");
INSERT INTO Events ("Date", "Name", "Info", "Time") VALUES ("19th January","New Years Coastal Hike", "Kick off your new years by discovering newport on January 1st", "10:00");



DROP TABLE if EXISTS LevelCoastalPath;
CREATE TABLE if not EXISTS "LevelCoastalPath" ( "Title" TEXT, "Vist" TEXT, "Info" TEXT);
INSERT INTO LevelCoastalPath ("Title", "Vist", "Info") VALUES ("Recomended for Avid Walkers", " - You will visit: Redwick, Whitson, Goldcliff SeaWall and Priory and, The Wetlands Centre ", "
The coast path runs adjacent to the Severn
Estuary for a distance of approximately 6.3 miles
which is generally flat. The majority of this
section of path has been established on top
of the sea defence, allowing easy walking and
rewarding walkers with striking views over the
estuary and the historic Gwent Levels landscape.
Much of the coast path and many link paths
around the reserve have been surfaced allowing
access for less able users.");

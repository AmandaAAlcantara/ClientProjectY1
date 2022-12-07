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
INSERT INTO RoutesC ("Picture", "Name", "Info") VALUES ("/static/Routes/CityCentre.jpg", "City Centre Walk", "Free entry perfect for an afternoon walk");
INSERT INTO RoutesC ("Picture", "Name", "Info") VALUES ("/static/Routes/RiverUsk.jpg", "River Usk Path", "Free entry perfect for an afternoon walk");
INSERT INTO RoutesC ("Picture", "Name", "Info") VALUES ("/static/Routes/Arcades.jpg", "Arcades, Cafes and Stores", "Free entry perfect for an afternoon walk");
INSERT INTO RoutesC ("Picture", "Name", "Info") VALUES ("/static/Routes/BoatClub.jpeg", "Newport Boat Club", "Free entry perfect for an afternoon walk");
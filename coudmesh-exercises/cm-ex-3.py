from cloudmesh.common.FlatDict import FlatDict

data = {
        # "caucus": null,
        "congress_numbers": [
            116,
            117,
            118
        ],
        # "current": true,
        "description": "Senior Senator for Ohio",
        # "district": null,
        "enddate": "2025-01-03",
        "extra": {
            "address": "503 Hart Senate Office Building Washington DC 20510",
            "contact_form": "http://www.brown.senate.gov/contact/",
            "office": "503 Hart Senate Office Building",
            "rss_url": "http://www.brown.senate.gov/rss/feeds/?type=all&amp;"
        },
        # "leadership_title": null,
        "party": "Democrat",
        "person": {
            "bioguideid": "B000944",
            "birthday": "1952-11-09",
            "cspanid": 5051,
            "firstname": "Sherrod",
            "gender": "male",
            "gender_label": "Male",
            "lastname": "Brown",
            "link": "https://www.govtrack.us/congress/members/sherrod_brown/400050",
            "middlename": "",
            "name": "Sen. Sherrod Brown [D-OH]",
            "namemod": "",
            "nickname": "",
            "osid": "N00003535",
            "pvsid": "27018",
            "sortname": "Brown, Sherrod (Sen.) [D-OH]",
            "twitterid": "SenSherrodBrown",
            "youtubeid": "SherrodBrownOhio"
        },
        "phone": "202-224-2315",
        "role_type": "senator",
        "role_type_label": "Senator",
        "senator_class": "class1",
        "senator_class_label": "Class 1",
        "senator_rank": "senior",
        "senator_rank_label": "Senior",
        "startdate": "2019-01-03",
        "state": "OH",
        "title": "Sen.",
        "title_long": "Senator",
        "website": "https://www.brown.senate.gov"
    }

flat = FlatDict(data, sep=".")

print(flat)
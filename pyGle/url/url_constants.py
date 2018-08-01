#
#                py-google-search  Copyright (C) 2018  Javinator9889                
#   This program comes with ABSOLUTELY NO WARRANTY; for details add the "-h" option.
#           This is free software, and you are welcome to redistribute it
#                 under certain conditions; type "-L" for details.
#

__google_base_url__ = "https://www.google.com/search?"
__google_url_modifiers__ = {
    "query": "q={0}",
    "in_order_displayed": "as_epq={0}",
    "or": "as_oq={0}",
    "exclude": "as_eq={0}",
    "number_of_results": "num={0}",
    "with_extension": "as_filetype={0}",
    "at_site": "as_sitesearch={0}",
    "with_time_limit": "as_qdr={0}",
    "with_time_limitation_for": {
        "day": 'd',
        "week": 'w',
        "month": 'm',
        "year": 'y'
    },
    "with_rights": "as_rights={0}",
    "with_rights_types": {
        "free_to_use": "(cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived)",
        "free_to_use_com": "(cc_publicdomain|cc_attribute|cc_sharealike|cc_nonderived).-(cc_noncommercial)",
        "free_to_use_and_modify": "(cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial).-(cc_nonderived)",
        "free_to_use_and_modify_com": "(cc_publicdomain|cc_attribute|cc_sharealike).-(cc_noncommercial|cc_nonderived)"
    },
    "with_licenses": ["cc_publicdomain", "cc_attribute", "cc_sharealike", "cc_noncommercial", "cc_nonderived"],
    "with_text_in_title": "allintitle%3A{0}",
    "with_text_in_body": "allintext%3A{0}",
    "with_text_in_url": "allinurl%3A{0}",
    "with_text_in_anchor": "allinanchor%3A{0}",
    "between_two_numbers": "{0}..{1}",
    "with_related_pages_to_a_doc": "as_rq={0}",
    "with_synonymous_searching": "~{0}",
    "with_defining": "define%3A{0}",
    "with_containing_two_terms": "{0}*{1}",
    "with_arithmetic_operation": {
        "sum": '+',
        "subtract": '-',
        "divide": '/',
        "multiply": '*',
        "power_of": '^',
        "percentage_of": '%'
    },
    "with_safe_active": "safe=active",
    "with_safe_deactivated": "safe=images",
    "with_linking_to_url": "as_lq={0}",
    "with_personalized_search": "pws=1",
    "with_no_personalized_search": "pws=0",
    "with_language_interface": "hl={0}",
    "with_results_language": "lr={0}",
    "with_languages": {
        "Arabic": "lang_ar",
        "Armenian": "lang_hy",
        "Belarusian": "lang_be",
        "Bulgarian": "lang_bg",
        "Catalan": "lang_ca",
        "Croatian": "lang_hr",
        "Czech": "lang_cs",
        "Danish": "lang_da",
        "Dutch": "lang_nl",
        "English": "lang_en",
        "Esperanto": "lang_eo",
        "Estonian": "lang_et",
        "Filipino": "lang_tl",
        "Finnish": "lang_fi",
        "French": "lang_fr",
        "German": "lang_de",
        "Greek": "lang_el",
        "Hebrew": "lang_iw",
        "Hungarian": "lang_hu",
        "Icelandic": "lang_is",
        "Indonesian": "lang_id",
        "Italian": "lang_it",
        "Japanese": "lang_ja",
        "Korean": "lang_ko",
        "Latvian": "lang_lv",
        "Lithuanian": "lang_lt",
        "Norwegian": "lang_no",
        "Persian": "lang_fa",
        "Polish": "lang_pl",
        "Portuguese": "lang_pt",
        "Romanian": "lang_ro",
        "Russian": "lang_ru",
        "Serbian": "lang_sr",
        "Slovak": "lang_sk",
        "Slovenian": "lang_sl",
        "Spanish": "lang_es",
        "Swedish": "lang_sv",
        "Thai": "lang_sv",
        "Turkish": "lang_tr",
        "Ukrainian": "lang_uk",
        "Vietnamese": "lang_vi",
        "Chinese Simplified": "lang_zh-CN",
        "Chinese Traditional": "lang_zh-TW"
    },
    "with_country_results": "cr=country{0}",
    "with_countries": {
        "Afghanistan": "AF",
        "Åland Islands": "AX",
        "Albania": "AL",
        "Algeria": "DZ",
        "American Samoa": "AS",
        "AndorrA": "AD",
        "Angola": "AO",
        "Anguilla": "AI",
        "Antarctica": "AQ",
        "Antigua and Barbuda": "AG",
        "Argentina": "AR",
        "Armenia": "AM",
        "Aruba": "AW",
        "Australia": "AU",
        "Austria": "AT",
        "Azerbaijan": "AZ",
        "Bahamas": "BS",
        "Bahrain": "BH",
        "Bangladesh": "BD",
        "Barbados": "BB",
        "Belarus": "BY",
        "Belgium": "BE",
        "Belize": "BZ",
        "Benin": "BJ",
        "Bermuda": "BM",
        "Bhutan": "BT",
        "Bolivia": "BO",
        "Bosnia and Herzegovina": "BA",
        "Botswana": "BW",
        "Bouvet Island": "BV",
        "Brazil": "BR",
        "British Indian Ocean Territory": "IO",
        "Brunei Darussalam": "BN",
        "Bulgaria": "BG",
        "Burkina Faso": "BF",
        "Burundi": "BI",
        "Cambodia": "KH",
        "Cameroon": "CM",
        "Canada": "CA",
        "Cape Verde": "CV",
        "Cayman Islands": "KY",
        "Central African Republic": "CF",
        "Chad": "TD",
        "Chile": "CL",
        "China": "CN",
        "Christmas Island": "CX",
        "Cocos (Keeling) Islands": "CC",
        "Colombia": "CO",
        "Comoros": "KM",
        "Congo": "CG",
        "Congo, Democratic Republic": "CD",
        "Cook Islands": "CK",
        "Costa Rica": "CR",
        "Cote D'Ivoire": "CI",
        "Croatia": "HR",
        "Cuba": "CU",
        "Cyprus": "CY",
        "Czech Republic": "CZ",
        "Denmark": "DK",
        "Djibouti": "DJ",
        "Dominica": "DM",
        "Dominican Republic": "DO",
        "Ecuador": "EC",
        "Egypt": "EG",
        "El Salvador": "SV",
        "Equatorial Guinea": "GQ",
        "Eritrea": "ER",
        "Estonia": "EE",
        "Ethiopia": "ET",
        "Falkland Islands (Malvinas)": "FK",
        "Faroe Islands": "FO",
        "Fiji": "FJ",
        "Finland": "FI",
        "France": "FR",
        "French Guiana": "GF",
        "French Polynesia": "PF",
        "French Southern Territories": "TF",
        "Gabon": "GA",
        "Gambia": "GM",
        "Georgia": "GE",
        "Germany": "DE",
        "Ghana": "GH",
        "Gibraltar": "GI",
        "Greece": "GR",
        "Greenland": "GL",
        "Grenada": "GD",
        "Guadeloupe": "GP",
        "Guam": "GU",
        "Guatemala": "GT",
        "Guernsey": "GG",
        "Guinea": "GN",
        "Guinea-Bissau": "GW",
        "Guyana": "GY",
        "Haiti": "HT",
        "Heard Island and Mcdonald Islands": "HM",
        "Holy See (Vatican City State)": "VA",
        "Honduras": "HN",
        "Hong Kong": "HK",
        "Hungary": "HU",
        "Iceland": "IS",
        "India": "IN",
        "Indonesia": "ID",
        "Iran": "IR",
        "Iraq": "IQ",
        "Ireland": "IE",
        "Isle of Man": "IM",
        "Israel": "IL",
        "Italy": "IT",
        "Jamaica": "JM",
        "Japan": "JP",
        "Jersey": "JE",
        "Jordan": "JO",
        "Kazakhstan": "KZ",
        "Kenya": "KE",
        "Kiribati": "KI",
        "Korea (North)": "KP",
        "Korea (South)": "KR",
        "Kosovo": "XK",
        "Kuwait": "KW",
        "Kyrgyzstan": "KG",
        "Laos": "LA",
        "Latvia": "LV",
        "Lebanon": "LB",
        "Lesotho": "LS",
        "Liberia": "LR",
        "Libyan Arab Jamahiriya": "LY",
        "Liechtenstein": "LI",
        "Lithuania": "LT",
        "Luxembourg": "LU",
        "Macao": "MO",
        "Macedonia": "MK",
        "Madagascar": "MG",
        "Malawi": "MW",
        "Malaysia": "MY",
        "Maldives": "MV",
        "Mali": "ML",
        "Malta": "MT",
        "Marshall Islands": "MH",
        "Martinique": "MQ",
        "Mauritania": "MR",
        "Mauritius": "MU",
        "Mayotte": "YT",
        "Mexico": "MX",
        "Micronesia": "FM",
        "Moldova": "MD",
        "Monaco": "MC",
        "Mongolia": "MN",
        "Montserrat": "MS",
        "Morocco": "MA",
        "Mozambique": "MZ",
        "Myanmar": "MM",
        "Namibia": "NA",
        "Nauru": "NR",
        "Nepal": "NP",
        "Netherlands": "NL",
        "Netherlands Antilles": "AN",
        "New Caledonia": "NC",
        "New Zealand": "NZ",
        "Nicaragua": "NI",
        "Niger": "NE",
        "Nigeria": "NG",
        "Niue": "NU",
        "Norfolk Island": "NF",
        "Northern Mariana Islands": "MP",
        "Norway": "NO",
        "Oman": "OM",
        "Pakistan": "PK",
        "Palau": "PW",
        "Palestinian Territory, Occupied": "PS",
        "Panama": "PA",
        "Papua New Guinea": "PG",
        "Paraguay": "PY",
        "Peru": "PE",
        "Philippines": "PH",
        "Pitcairn": "PN",
        "Poland": "PL",
        "Portugal": "PT",
        "Puerto Rico": "PR",
        "Qatar": "QA",
        "Reunion": "RE",
        "Romania": "RO",
        "Russian Federation": "RU",
        "Rwanda": "RW",
        "Saint Helena": "SH",
        "Saint Kitts and Nevis": "KN",
        "Saint Lucia": "LC",
        "Saint Pierre and Miquelon": "PM",
        "Saint Vincent and the Grenadines": "VC",
        "Samoa": "WS",
        "San Marino": "SM",
        "Sao Tome and Principe": "ST",
        "Saudi Arabia": "SA",
        "Senegal": "SN",
        "Serbia": "RS",
        "Montenegro": "ME",
        "Seychelles": "SC",
        "Sierra Leone": "SL",
        "Singapore": "SG",
        "Slovakia": "SK",
        "Slovenia": "SI",
        "Solomon Islands": "SB",
        "Somalia": "SO",
        "South Africa": "ZA",
        "South Georgia and the South Sandwich Islands": "GS",
        "Spain": "ES",
        "Sri Lanka": "LK",
        "Sudan": "SD",
        "Suriname": "SR",
        "Svalbard and Jan Mayen": "SJ",
        "Swaziland": "SZ",
        "Sweden": "SE",
        "Switzerland": "CH",
        "Syrian Arab Republic": "SY",
        "Taiwan, Province of China": "TW",
        "Tajikistan": "TJ",
        "Tanzania": "TZ",
        "Thailand": "TH",
        "Timor-Leste": "TL",
        "Togo": "TG",
        "Tokelau": "TK",
        "Tonga": "TO",
        "Trinidad and Tobago": "TT",
        "Tunisia": "TN",
        "Turkey": "TR",
        "Turkmenistan": "TM",
        "Turks and Caicos Islands": "TC",
        "Tuvalu": "TV",
        "Uganda": "UG",
        "Ukraine": "UA",
        "United Arab Emirates": "AE",
        "United Kingdom": "GB",
        "United States": "US",
        "United States Minor Outlying Islands": "UM",
        "Uruguay": "UY",
        "Uzbekistan": "UZ",
        "Vanuatu": "VU",
        "Venezuela": "VE",
        "Viet Nam": "VN",
        "Virgin Islands, British": "VG",
        "Virgin Islands, U.S.": "VI",
        "Wallis and Futuna": "WF",
        "Western Sahara": "EH",
        "Yemen": "YE",
        "Zambia": "ZM",
        "Zimbabwe": "ZW"
    },
    "with_document_county": "gl={0}",
    "with_extra_attributes": "tbs={0}",
    "with_search_between_two_dates": "cdr:1,cd_min:{0},cd_max:{1}",
    "with_search_between_two_dates_by_update_time": "sbd:1,cd_min:{0},cd_max:{1}",
    "with_search_by_update_time": "sbd:1",
    "with_searching_at_different_google_pages": "tbm={0}",
    "with_searching": {
        "apps": "app",
        "books": "book",
        "images": "isch",
        "news": "nws",
        "patents": "pts",
        "shops": "shop",
        "videos": "vid"
    },
    "with_starting_at_position": "start={0}",
    "with_image_params": {
        "color": {
            "red": "ic:specific,isc:red",
            "orange": "ic:specific,isc:orange",
            "yellow": "ic:specific,isc:yellow",
            "green": "ic:specific,isc:green",
            "teal": "ic:specific,isc:teel",
            "blue": "ic:specific,isc:blue",
            "purple": "ic:specific,isc:purple",
            "pink": "ic:specific,isc:pink",
            "white": "ic:specific,isc:white",
            "gray": "ic:specific,isc:gray",
            "black": "ic:specific,isc:black",
            "brown": "ic:specific,isc:brown"
        },
        "color_type": {
            "full-color": "ic:color",
            "black-and-white": "ic:gray",
            "transparent": "ic:trans"
        },
        "image_rights": {
            "labeled-for-reuse-with-modifications": "sur:fmc",
            "labeled-for-reuse": "sur:fc",
            "labeled-for-noncommercial-reuse-with-modification": "sur:fm",
            "labeled-for-noncommercial-reuse": "sur:f"
        },
        "image_size": {
            "large": "isz:l",
            "medium": "isz:m",
            "icon": "isz:i",
            ">400*300": "isz:lt,islt:qsvga",
            ">640*480": "isz:lt,islt:vga",
            ">800*600": "isz:lt,islt:svga",
            ">1024*768": "visz:lt,islt:xga",
            ">2MP": "isz:lt,islt:2mp",
            ">4MP": "isz:lt,islt:4mp",
            ">6MP": "isz:lt,islt:6mp",
            ">8MP": "isz:lt,islt:8mp",
            ">10MP": "isz:lt,islt:10mp",
            ">12MP": "isz:lt,islt:12mp",
            ">15MP": "isz:lt,islt:15mp",
            ">20MP": "isz:lt,islt:20mp",
            ">40MP": "isz:lt,islt:40mp",
            ">70MP": "isz:lt,islt:70mp"
        },
        "image_type": {
            "face": "itp:face",
            "photo": "itp:photo",
            "clip-art": "itp:clip-art",
            "line-drawing": "itp:lineart",
            "animated": "itp:animated"
        },
        "aspect_ratio": {
            "tall": "iar:t",
            "square": "iar:s",
            "wide": "iar:w",
            "panoramic": "iar:xw"
        },
        "format": {
            "jpg": "ift:jpg",
            "gif": "ift:gif",
            "png": "ift:png",
            "bmp": "ift:bmp",
            "svg": "ift:svg",
            "webp": "webp",
            "ico": "ift:ico"
        }
    },
    "with_patents_params": {
        "with_search_at_patent_office": "ptso:{0}",
        "with_office_patents": {
            "EE.UU.": "us",
            "Europe": "ep",
            "International": "wo",
            "China": "cn",
            "Germany": "de",
            "Canada": "ca"
        },
        "with_patent_status": "ptss:{0}",
        "with_available_status": {
            "Applications": "a",
            "Issued patents": "g"
        },
        "with_patent_type": "ptst:{0}",
        "with_available_patent_types": {
            "Utility": "u",
            "Design": "d",
            "Plant": "pp",
            "Defensive Publication": "t",
            "Additional Improvement": "ai",
            "Statutory Invention Registration": "h"
        }
    },
    "with_shop_params": {
        "only_new_products": "new:1",
        "with_custom_price": "price:1",
        "with_max_price": "ppr_max:{0}",
        "with_min_price": "ppr_min:{0}",
        "sort_order_less_to_high": "p_ord:p",
        "sort_order_high_to_less": "p_ord:pd",
        "sort_order_reviews": "p_ord:rv"
    }
}

__user_agents__ = {
    "chrome": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/41.0.2228.0 Safari/537.36",
    "edge": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
    "firefox": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
    "safari": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) "
              "Version/7.0.3 Safari/7046A194A"
}

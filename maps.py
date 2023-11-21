google_forms_link="https://docs.google.com/forms/d/e/1FAIpQLSeh0sXAiydhwsqM1nHz4It9XtDyLFhOrt9GN850xmhvocdCqQ/viewform?usp=pp_url"

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome()
import time
latitudes=[16.852522,
16.852959,
16.85322,
16.853234,
16.853656,
16.856195,
16.857985,
16.859611,
16.861352,
16.863053,
16.864304,
16.865146,
16.865998,
16.86682,
16.867711,
16.868607,
16.869364,
16.870228,
16.871217,
16.871976,
16.873275,
16.874806,
16.876242,
16.87759,
16.878614,
16.87963,
16.880547,
16.881386,
16.88252,
16.883483,
16.884388,
16.886446,
16.888033,
16.890055,
16.891959,
16.893861,
16.895679,
16.896049,
16.896476,
16.897105,
16.897726,
16.898363,
16.898256,
]
longitudes=[79.9049329,
79.904833,
79.904886,
79.904888,
79.905094,
79.904936,
79.90248,
79.900247,
79.897858,
79.895511,
79.893505,
79.890922,
79.888261,
79.885761,
79.883039,
79.880254,
79.877884,
79.875194,
79.872202,
79.869847,
79.8675,
79.864814,
79.862241,
79.85988,
79.857949,
79.855406,
79.853147,
79.850905,
79.848048,
79.845632,
79.843264,
79.840937,
79.839118,
79.836717,
79.834538,
79.832347,
79.83015,
79.827892,
79.825497,
79.824575,
79.823397,
79.823962,
79.8240752,
]
locations=["G",
1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20,
21,
22,
23,
24,
25,
26,
27,
28,
29,
30,
31,
32,
33,
34,
35,
36,
37,
38,
39,
40,
41,
"G"
]
map_link=['http://maps.google.com/maps?q=16.852522,79.9049329', 'http://maps.google.com/maps?q=16.852959,79.904833', 'http://maps.google.com/maps?q=16.85322,79.904886', 'http://maps.google.com/maps?q=16.853234,79.904888', 'http://maps.google.com/maps?q=16.853656,79.905094', 'http://maps.google.com/maps?q=16.856195,79.904936', 'http://maps.google.com/maps?q=16.857985,79.90248', 'http://maps.google.com/maps?q=16.859611,79.900247', 'http://maps.google.com/maps?q=16.861352,79.897858', 'http://maps.google.com/maps?q=16.863053,79.895511', 'http://maps.google.com/maps?q=16.864304,79.893505', 'http://maps.google.com/maps?q=16.865146,79.890922', 'http://maps.google.com/maps?q=16.865998,79.888261', 'http://maps.google.com/maps?q=16.86682,79.885761', 'http://maps.google.com/maps?q=16.867711,79.883039', 'http://maps.google.com/maps?q=16.868607,79.880254', 'http://maps.google.com/maps?q=16.869364,79.877884', 'http://maps.google.com/maps?q=16.870228,79.875194', 'http://maps.google.com/maps?q=16.871217,79.872202', 'http://maps.google.com/maps?q=16.871976,79.869847', 'http://maps.google.com/maps?q=16.873275,79.8675', 'http://maps.google.com/maps?q=16.874806,79.864814', 'http://maps.google.com/maps?q=16.876242,79.862241', 'http://maps.google.com/maps?q=16.87759,79.85988', 'http://maps.google.com/maps?q=16.878614,79.857949', 'http://maps.google.com/maps?q=16.87963,79.855406', 'http://maps.google.com/maps?q=16.880547,79.853147', 'http://maps.google.com/maps?q=16.881386,79.850905', 'http://maps.google.com/maps?q=16.88252,79.848048', 'http://maps.google.com/maps?q=16.883483,79.845632', 'http://maps.google.com/maps?q=16.884388,79.843264', 'http://maps.google.com/maps?q=16.886446,79.840937', 'http://maps.google.com/maps?q=16.888033,79.839118', 'http://maps.google.com/maps?q=16.890055,79.836717', 'http://maps.google.com/maps?q=16.891959,79.834538', 'http://maps.google.com/maps?q=16.893861,79.832347', 'http://maps.google.com/maps?q=16.895679,79.83015', 'http://maps.google.com/maps?q=16.896049,79.827892', 'http://maps.google.com/maps?q=16.896476,79.825497', 'http://maps.google.com/maps?q=16.897105,79.824575', 'http://maps.google.com/maps?q=16.897726,79.823397', 'http://maps.google.com/maps?q=16.898363,79.823962', 'http://maps.google.com/maps?q=16.898256,79.8240752']

for n in range(len(latitudes)):
    driver.get(google_forms_link)
    time.sleep(5)
    latitude=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    latitude.send_keys(latitudes[n])
    longitude = driver.find_element(By.XPATH,
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    longitude.send_keys(longitudes[n])

    location = driver.find_element(By.XPATH,
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    location.send_keys(locations[n])

    loc_link = driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    loc_link.send_keys(map_link[n])



    submit=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()
import urllib.request
import urllib.parse
import re
import get_weather
import pandas as pd
import model


def get_ytlink(search_keyword):
    # html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    # video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    # print("video",video_ids)

    link_address = ("https://www.youtube.com/embed/"+search_keyword)
    return link_address


def song_playlist(songList):

    songs_link = list()
    for song_id in songList:
        # print(song_id)
        songs_link.append(get_ytlink(song_id))

    return songs_link



def get_genre(genre1, genre2, genre3):

    genre_dic = {
        '힙합' : ['vYRCBrY5KNk', 'JX_oH8amzOI', 'oCqpdihI0_4', 'K4tgU1JN6P8', '0KvNmjYU7fY', '9VyK8M5gNt0', 'vdZ6SW6CXCQ', 'H52OZEXtEnQ', 'YlKY4EImAWM', 'CIu2g17Bubk', '9ygI-ARlYVI', '3f5NfQV8s7o', 'TJ5x_tDgrZE', 'wlbDK3PHcLI', 'NE14c5mEUdU', 'QbjNWULcdwI', '0kgii7qQwWQ', '9s5s7QuAYsk', 'ecKEnrWIh7Q', '81kzxCNBKM4', 'hYuDceLh69g', 'e9FDun2_j7Y', 'Gg3EHytbROU', 'nAtTxQTMHAo', 'nx59bl-BB1o', '34FubFtNC5g', 'g5tA599ejgI', 'u4wOdsbgbMs', 'QK3Q6igbvhA', 'XI3O0qO_XyY', '1Oi12PBSlgk', 'n9svf5QwfE0', 'A0yntW5zRg8', 'XHHylBt_J74', '4UHcxwgifkA'] ,
        '기타' : ['rnidk5D8zXg', 'rdLk2QBzvtc', '40C_kbazS4k', '53Icr-FluPs', 'nt8kA3_5Igc', 'jbK68mHsLfg', '8M80_logcOQ', 'cFc99sHqBTU', '-6RqR2PCHQs', 'VHDvG3bvkW4', 'MFj42lBdJXU', 'zPVA2J_8Rp0', 'djQRh-RjILo', 'BlZ2kw1_xfw', 'LZ_WlubEQc0', 'iITAUEE9Ja0', '0mCQxNXT8A4', 'n8n1YUVF7IA', '5U3gX9Qk4yk', 'css1gXopHfg', 'PW6Gps7J-DM', 'aFLVzk-12Zk', 'E2k-at-JWHw', 'zZN7Q9wg7-E', '70HO9Ga6IAY', 'tKdJHWo-kLI', 'pt13BTQ4smE', 'SmTRaSg2fTQ', 'nvhC-sfNqL4', 'h1tTGsPp7kY', '6gb9aV7nG_g', 'lWY-5oeLTL4', '1W0OA_l9LiQ', 'krIHTd-7PGY', 'v5Xff5p4VcM', 'teXv84f56TI', 'nddpbzfX8CQ'] ,
        '댄스' : ['75tay629QyQ', 'J2fclJEcGXQ', '8iaJA_Fs_w8', 'RYK2Rrysqeg', 'y0vcpL6GnyE', 'W5dzCop4tzU', 'F_wfPMaLeXs', 'jXaHDtZSR70', 'RaNiHfXCp8A', '91pQYxPqK2Q', 'CDgxtFjjI2w', 'dOQhvvNHAFk', 'm0HS45AygzM', 'cj4AX1KLHVg', '3Hn_kp_Fxkg', 'g_8062N5zQs', 'W50T9G-O7gU', 'xMgicLWUebg', 'BMlmUnXSDy8', 'vhvU0-TU6Zc', 'yMvy2JGGvxw', 'EYQJ1jnP-I8', 'izunivHWztc', 'fi7sBXorcC4', 'ZvtzcQJaYJQ', 'YD5QQLhhCyQ', 'mazPt-kEoUE', 'dthmyYUi7Es', 'FMO377gw8F8', '1pi92Bbi4DQ', 'lVdi1jaTxlc', 'g4YccawSQ1g', '5u84jGWJxj0', 'EvW2Rjjyxn0'] ,
        '발라드' : ['kp573-v625Y', 'AAf8cME5STM', 'eqfFj7OJ1u4', '98jt_U0jJ7E', '4a5yL9Bc4_o', 'SiD0WinCeIo', 'OzSs_Zj3VrM', 'qMQMqDp0WRM', 'jyzo8G6yMAc', 'PO0tqIuPJGw', 'dOQhvvNHAFk', 'bhDOqCR61jU', 'ZuGf78HgZRE', 'hAopzWKVdX4', 'SJAjezgTBZw', 'ADi66Vt5jK8', 'MaQiJRMwJEw', 'CIvrCQ6alyM', 'GRIMTo9Kyrk', 'GqNmImL-dgw', 'jF7tuqxE0Gs', 'z1QZVhLFsWc', 'lDp-XgVTuqA', '4uq8r6Czxl0', 'nt8kA3_5Igc', 'ecgp5SZgKHU', 'gR37CrZT-kY', 'TcUYr4iokTg', '3OWljFqxfgY', 'leIeBhYYJP0', 'K-jaMXMYTkk', 'sLl2Bx-aerA', 'HAaTY6BrIGg', 'zRc5o3NXHE4', 'Ap7IAeNC4Ws', 'C_q2duwuPFw', '5f2AFS6PgEs', 'l8nngQsCOc0', 'IDD5_z3kKCU', '_Xfw7J9Hv7E', '-d5xM1C1tlo', '0aPgAMC_xLw', 'lVdi1jaTxlc', 'lcFQqLrgPpA', 'JRgUXhQqO3w', '8hGp4HRS-i8', 'wD3l5vONVR0', 'hEWfJLMvx1A', 'jukpx3vpRG4', '0189i1ripvE', 'DKNXjcJ9k6A', 'ZjqInVMdzQY', 'NEpZoGoQEUk', 'gRAjH-FSofA', 'kmLmsXqL6BI', 'ed0CcFcBBMI', '8AGToyVpTXA', 'A3ETK4WJvVo', 'tr-GNtoT810', '75tay629QyQ', 'PZynBaYrdpU', '_EfRa_ywkEw', '79y4Ld2_yt8', 'Wtuxke576mo', 'xQSTdR3Po28', 'vQHqAfc6Mjk', 'yFLA3AotTHk', 'OaOeMJnFTPU', '39NWW8Q3mIk', 'Hc4utd--utk', '92f_BNFNHNw', '36S6frKMXX8', 'CTYd-2pWXpM', 'jM6WLmFNlYg', 'scXuReCe2Co', 'KnsIQFrPWHw', 'QkAyVvtApKs', 'iONBZvzaFso', 'QKm99bWL3TQ', '8L-MINLlMIc', 'bhT59fGmjms', 'Emgq96oOKPw', 'dGbV6VUvsFU', 'cLpO0U3p97c', 'xz4eOlHJS60'] ,
        '락' : ['1tJhYWaHyhE', 'UO3RLLoWGLA', '6FyN34oVD-w', '9zX6fljTfEw', 'uUwiFtXsh7Q', '2n38FXtnv7Q', 'vrybNsmdg2Q', 'WOGAwenS9oQ', 'Le85YH7K_mE', '32PKh_5GPnI', '5i19X5bPHNI', 'pnlZjGlCchA', 'qVy8nB_hT18', 'bIoZgT3z1d0', 'kFkp8JrkPsQ', 'NAKsWDdxo5k', '-K8sOQMbt2Y', 'Q1hOBbSdIYo', 'huWdaVJS8yY', '1gABYdLOQpY', 'DZ6A7YAzAZA', '4jVJxPLo4Jg', '3UlDGZAHU4Y', 'L4TtasY-QTo', 'ZSat_xY9pcU', 'Smzcq1E6bDU', 'w5cbKQdFY44', '0N2qS-O-uxo', '3sqRS_wqwBQ', 'ATdl1_lyAbI', 'hWCQcQqTLhg', '2zHjtH-6Oho', 'prflhTQah9w', 'v-TBS3qrQhI', '5yIFrqY8JHk', 'b7fkx4VZuXg', 'TT9JkgZoiuY', 'OJFu4STrVH0', '5H6woZUYeHQ', 'Ge2oip3tmQA', 'tXWVFXkMhcE', 'GjgZkEBZ-LE', 'mC57r3dronE', 'K5IdTqP70Us', 'p735iJXDVTI', '9CZaYE0pBNs', 'rhrFqwPYwig', 'z32h2JUiGzA', '_ThBN0zMM9g'] ,
        '재즈' : ['40C_kbazS4k', 'abmuyFkCka0', '2J8IUUtmLE0', 'l2bLKltY8Lo', 'vhvU0-TU6Zc', 'B48V42s3dnc', 'XJF5GaZ_GBU', '4L0lylBK8gE', 'gHcCZzk4pxk', 'LNhB9uZnIBw', '26V04Q5_jJQ', '7_lopC6G_yk', '53Icr-FluPs', 'xxFK3evO7p8', '3auRYESQkGw', 'JkXu2yE199g', 'iwrrqrRVWBA', 'H52OZEXtEnQ', '6UxLDsT2VTk', 'K8DFpdCkdns', 'GptkdoVohr4', 'sLl2Bx-aerA', 'JbmxSxxRl9Y', '_kcw0ITkOKA', 'hl16iyDGa6E', 'A76AhZxOV_c', 'duCMwFOKtiE', '7Vwc2o6is6o', 'BHb-B0XEF14', 'IDD5_z3kKCU', 'l6NxV5fcdkg', 'oLR7OAaxKaY', 'xkytDbjvi0c', 'jQW3StI6fmQ', 'ldY9mGCcql4', 'TFRPcnw_oqY', 'ZRUiNvCMgc4', '3L23oeGRWgQ', 'dVUJN3n4ePk', 'hm33x3jVO70', 'u-CCHDQVzr4', 'm32duJnYsvI', 'wcO3ZXm3oSc', 'VMJS2aIpFtQ', 'RlcShLzSLxc', 'TfyUUvhb_vs', 'LSpINqHE66g', 'fhcY68lCQNU', 'UOHy5Sc0gTs', 'FhbCZ51HM8E', 'USdGpAfazcg', '8ysfAJZlqWE', 'KIVP4USaVJk', 'j5ZUbKz7cPQ', 'EXRjvh3-NFs', 'SR-12BXlt88', 'UmXwB1jiWD8', 'L3Zyj2HU9tI', '3EFUbX0RKY4', 'VxwprP-O0So', 'pt_rU-ZC_7o', 'Tgb5Pdqt-A0', 'UAHP1VgljnE', 'zV8HByBA3_8', '-Rc-6VMKydA', 'EXyeamh3Mbw', 'ta_4hBWwlXU', '2Td_w5WXYnI', 'nDRz01TrjgY', 'mdskEOdONAg', 'QkAyVvtApKs', 'V1AbF_fnTq0', 'uR2h1hCJ-zg', '3OJicL9tdOU', 'hqvE4Xwc3ts', 'eAngyUowXvg', 'fNrF4v9MfIg', 'nj9xmK11vPs']
        }

    return genre_dic[genre1] + genre_dic[genre2] + genre_dic[genre3]

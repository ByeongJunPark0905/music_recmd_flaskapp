import pickle
import joblib
import pandas as pd
import numpy as np

import random
import get_weather
import get_songs

'재추천 코드는 주석처리한 상태'

def playlist_get(tags):
    playlist_dic = {
        0: ['cLpO0U3p97c', '-6RqR2PCHQs', 'leIeBhYYJP0', 'sLl2Bx-aerA', 'tKdJHWo-kLI', 'bhDOqCR61jU', 'iwrrqrRVWBA',
            '5f2AFS6PgEs', '_ThBN0zMM9g', 'vrybNsmdg2Q', 'lDp-XgVTuqA', 'CIvrCQ6alyM', 'rhrFqwPYwig', '3Hn_kp_Fxkg',
            'K-jaMXMYTkk', 'B48V42s3dnc', 'ecKEnrWIh7Q', 'scXuReCe2Co', 'UAHP1VgljnE'],
        1: ['dOQhvvNHAFk', 'L3Zyj2HU9tI', '6UxLDsT2VTk', 'hm33x3jVO70', '8L-MINLlMIc', '39NWW8Q3mIk', 'GRIMTo9Kyrk',
            'gHcCZzk4pxk', 'kmLmsXqL6BI', 'lVdi1jaTxlc', 'CTYd-2pWXpM', '53Icr-FluPs'],
        2: ['F_wfPMaLeXs', '36S6frKMXX8', 'IDD5_z3kKCU', 'eqfFj7OJ1u4', 'zRc5o3NXHE4', 'kmLmsXqL6BI', 'vhvU0-TU6Zc',
            'NE14c5mEUdU', '40C_kbazS4k', '75tay629QyQ', 'QkAyVvtApKs', 'RaNiHfXCp8A'],
        3: ['cLpO0U3p97c', 'PO0tqIuPJGw', 'z1QZVhLFsWc', 'nt8kA3_5Igc', 'cFc99sHqBTU', '0189i1ripvE', 'Tgb5Pdqt-A0',
            'vQHqAfc6Mjk', '5f2AFS6PgEs', 'MaQiJRMwJEw', 'vhvU0-TU6Zc', '75tay629QyQ'],
        4: ['5i19X5bPHNI', 'EvW2Rjjyxn0', 'JX_oH8amzOI', 'xMgicLWUebg', 'hYuDceLh69g', 'b7fkx4VZuXg', 'Smzcq1E6bDU',
            '-d5xM1C1tlo', 'hWCQcQqTLhg', 'BHb-B0XEF14', 'C_q2duwuPFw', '_kcw0ITkOKA', '0N2qS-O-uxo', 'gHcCZzk4pxk',
            '53Icr-FluPs', 'LNhB9uZnIBw', 'jyzo8G6yMAc', 'BlZ2kw1_xfw', 'v-TBS3qrQhI', 'J2fclJEcGXQ', 'KnsIQFrPWHw',
            '-Rc-6VMKydA', 'uR2h1hCJ-zg', 'l8nngQsCOc0'],
        5: ['jF7tuqxE0Gs', 'dVUJN3n4ePk', '9zX6fljTfEw', 'gRAjH-FSofA', 'JRgUXhQqO3w', 'yMvy2JGGvxw', '8M80_logcOQ',
            'nj9xmK11vPs', '8iaJA_Fs_w8', 'hAopzWKVdX4', 'cFc99sHqBTU', 'v5Xff5p4VcM', '7Vwc2o6is6o', '70HO9Ga6IAY',
            'z32h2JUiGzA', 'K4tgU1JN6P8', 'RYK2Rrysqeg', 'EYQJ1jnP-I8', '75tay629QyQ', 'xkytDbjvi0c', 'dthmyYUi7Es',
            'ed0CcFcBBMI', 'W50T9G-O7gU', 'fhcY68lCQNU', 'YD5QQLhhCyQ', 'css1gXopHfg'],
        6: ['3OJicL9tdOU', 'IDD5_z3kKCU', '81kzxCNBKM4', 'Le85YH7K_mE', 'nvhC-sfNqL4', 'JbmxSxxRl9Y', 'huWdaVJS8yY',
            'abmuyFkCka0', 'dOQhvvNHAFk', 'PZynBaYrdpU', '0mCQxNXT8A4', '6FyN34oVD-w', 'ZvtzcQJaYJQ', 'y0vcpL6GnyE',
            'BMlmUnXSDy8', 'TFRPcnw_oqY', 'ZSat_xY9pcU', 'ldY9mGCcql4', 'jXaHDtZSR70', 'Gg3EHytbROU', 'wcO3ZXm3oSc',
            'MFj42lBdJXU', '_EfRa_ywkEw', 'zV8HByBA3_8', 'krIHTd-7PGY', 'mC57r3dronE', '2zHjtH-6Oho', 'pnlZjGlCchA',
            'VxwprP-O0So', '5u84jGWJxj0', 'KIVP4USaVJk', 'VHDvG3bvkW4'],
        7: ['91pQYxPqK2Q', 'QKm99bWL3TQ', '-K8sOQMbt2Y', 'mazPt-kEoUE', 'sLl2Bx-aerA', 'g_8062N5zQs', 'RlcShLzSLxc',
            'L4TtasY-QTo', 'tr-GNtoT810', 'V1AbF_fnTq0', 'Ap7IAeNC4Ws', 'qMQMqDp0WRM', '_Xfw7J9Hv7E', 'SR-12BXlt88',
            'm0HS45AygzM', 'l6NxV5fcdkg', 'SmTRaSg2fTQ', 'g4YccawSQ1g', 'Ge2oip3tmQA', 'n9svf5QwfE0', 'XHHylBt_J74',
            'jukpx3vpRG4', 'SJAjezgTBZw', 'oLR7OAaxKaY', 'FMO377gw8F8', 'LSpINqHE66g', 'ATdl1_lyAbI', '8ysfAJZlqWE',
            'bIoZgT3z1d0', '4jVJxPLo4Jg', 'Q1hOBbSdIYo', 'qVy8nB_hT18', 'WOGAwenS9oQ', 'EXyeamh3Mbw', 'prflhTQah9w',
            'fi7sBXorcC4', 'MaQiJRMwJEw', 'u4wOdsbgbMs'],
        8: ['VMJS2aIpFtQ', '5yIFrqY8JHk', '6gb9aV7nG_g', 'GjgZkEBZ-LE', '0KvNmjYU7fY', '3L23oeGRWgQ', 'djQRh-RjILo',
            'OzSs_Zj3VrM', '8hGp4HRS-i8', 'h1tTGsPp7kY', 'UOHy5Sc0gTs', 'jM6WLmFNlYg', 'vrybNsmdg2Q', 'QkAyVvtApKs',
            'Wtuxke576mo', '2n38FXtnv7Q', 'K8DFpdCkdns', 'CDgxtFjjI2w', 'aFLVzk-12Zk', '3UlDGZAHU4Y', 'bhT59fGmjms',
            'OaOeMJnFTPU'],
        9: ['8AGToyVpTXA', '5U3gX9Qk4yk', '7_lopC6G_yk', '3EFUbX0RKY4', 'teXv84f56TI', 'XJF5GaZ_GBU', 'nddpbzfX8CQ',
            '1pi92Bbi4DQ', 'gR37CrZT-kY', 'JkXu2yE199g', 'SiD0WinCeIo', 'w5cbKQdFY44', 'j5ZUbKz7cPQ', 'ta_4hBWwlXU'],
        10: ['g5tA599ejgI', 'hqvE4Xwc3ts', 'rdLk2QBzvtc', '98jt_U0jJ7E', '40C_kbazS4k', '4UHcxwgifkA', '0mCQxNXT8A4',
             'E2k-at-JWHw', 'USdGpAfazcg', 'p735iJXDVTI', 'eAngyUowXvg', 'GqNmImL-dgw', 'zPVA2J_8Rp0', 'OJFu4STrVH0',
             'jbK68mHsLfg', '92f_BNFNHNw', 'jQW3StI6fmQ', 'zZN7Q9wg7-E', '3f5NfQV8s7o', '2J8IUUtmLE0', 'DKNXjcJ9k6A',
             'vdZ6SW6CXCQ'],
        11: ['NAKsWDdxo5k', '32PKh_5GPnI', 'nAtTxQTMHAo', 'nt8kA3_5Igc', 'A3ETK4WJvVo', 'FhbCZ51HM8E', 'kFkp8JrkPsQ',
             '1gABYdLOQpY', 'rnidk5D8zXg', 'W5dzCop4tzU'],
        12: ['H52OZEXtEnQ', 'LZ_WlubEQc0', 'mdskEOdONAg', 'l2bLKltY8Lo', '1tJhYWaHyhE', 'kp573-v625Y', 'ecgp5SZgKHU',
             'cj4AX1KLHVg', 'pt_rU-ZC_7o', 'zPVA2J_8Rp0', 'nx59bl-BB1o', 'vrybNsmdg2Q', '34FubFtNC5g', 'u-CCHDQVzr4',
             'lVdi1jaTxlc', '4uq8r6Czxl0', 'tXWVFXkMhcE', 'n8n1YUVF7IA', 'oCqpdihI0_4', 'TT9JkgZoiuY', 'm32duJnYsvI',
             'NEpZoGoQEUk', 'Hc4utd--utk', 'ZuGf78HgZRE', 'ADi66Vt5jK8', 'xxFK3evO7p8'],
        13: ['26V04Q5_jJQ', 'ZRUiNvCMgc4', 'DZ6A7YAzAZA', 'xQSTdR3Po28', 'GptkdoVohr4', '79y4Ld2_yt8', '2Td_w5WXYnI',
             '4a5yL9Bc4_o', 'lcFQqLrgPpA', 'A0yntW5zRg8', 'HAaTY6BrIGg', 'A76AhZxOV_c', 'yFLA3AotTHk', '9ygI-ARlYVI',
             'dGbV6VUvsFU', '1W0OA_l9LiQ', 'UO3RLLoWGLA', 'PW6Gps7J-DM'],
        14: ['H52OZEXtEnQ', 'K5IdTqP70Us', 'pt13BTQ4smE', '3auRYESQkGw', '9s5s7QuAYsk', 'CIu2g17Bubk', 'TJ5x_tDgrZE',
             '1Oi12PBSlgk', 'wD3l5vONVR0', '3OWljFqxfgY', 'lWY-5oeLTL4', 'nDRz01TrjgY', 'YlKY4EImAWM', 'uUwiFtXsh7Q',
             'hEWfJLMvx1A', 'Emgq96oOKPw'],
        15: ['xz4eOlHJS60', 'iITAUEE9Ja0', '9CZaYE0pBNs', 'wlbDK3PHcLI', 'EXRjvh3-NFs', 'TfyUUvhb_vs', 'duCMwFOKtiE',
             'TcUYr4iokTg', '4UHcxwgifkA', '3sqRS_wqwBQ', 'ZjqInVMdzQY', 'QbjNWULcdwI', 'vYRCBrY5KNk', 'zRc5o3NXHE4',
             'hl16iyDGa6E', 'QK3Q6igbvhA', '9VyK8M5gNt0', '0aPgAMC_xLw', '4L0lylBK8gE', 'izunivHWztc', '2n38FXtnv7Q',
             'aFLVzk-12Zk', 'UmXwB1jiWD8', '0kgii7qQwWQ', 'XI3O0qO_XyY', 'fNrF4v9MfIg', 'iONBZvzaFso', '5H6woZUYeHQ',
             'AAf8cME5STM', 'e9FDun2_j7Y', 'u4wOdsbgbMs']
    }
    playlists = []
    for tag in tags:
        for playlist in playlist_dic:  # playlist는 playlist_dic의 키 값
            if playlist == tag:  # playlist_dic의 키와 input된 tag가 일치하는 경우
                playlists += playlist_dic[tag]  # 키가 tag인 playlist를 넣어준다.

    return playlists

def trans_input_to_num(t1, t2, t3, t4, t5):
    print("trans_input_num:",t1, t2, t3, t4, t5)
    taglist = []
    climate_dic = {'맑음': 1, '흐림': 3, '비': 2, '눈': 0}
    time_dic = {'오전': 1, '오후': 2, '저녁': 3, '밤': 0}
    gender_dic = {'남자': 0, '여자': 1}
    age_dic = {'10': 0, '20': 1, '30': 2, '40': 3, '50': 4}
    genre_dic = {'락': 2, '재즈': 5, '힙합': 6, '발라드': 4, '기타': 0, '댄스': 1, '랩': 3}

    taglist.append(climate_dic[str(t1)])
    taglist.append(time_dic[str(t2)])
    taglist.append(gender_dic[str(t3)])
    taglist.append(age_dic[str(t4)])
    taglist.append(genre_dic[str(t5)])

    return taglist


def tags_for_rec(taglist):
    cli_model = joblib.load('CLI2_model.pkl')
    x_test = pd.DataFrame(taglist)
    predict = cli_model.predict(x_test.transpose())

    return int(predict)


def recommendation(t1, t2, t3= '여자', t4= '20', g1='재즈', g2='재즈', g3='재즈'):
    print("recommend:",t3,t4,g1,g2,g3)
    genre = [g1, g2, g3]
    final_taglist = []
    for i in range(len(genre)):
        trans_list = trans_input_to_num(t1, t2, t3, t4, genre[i])
        print("trans list",trans_list)
        tag_list = tags_for_rec(trans_list)
        print("tag_list",tag_list)
        final_taglist.append(tag_list)
    final_taglist = (list(set(final_taglist)))

    result = playlist_get(final_taglist)


    return result



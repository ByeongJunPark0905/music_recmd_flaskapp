def playlist_get(tag):
    playlist_dic = {
        0: ['bhDOqCR61jU', 'leIeBhYYJP0', 'CIvrCQ6alyM', 'lDp-XgVTuqA', 'K-jaMXMYTkk', '-6RqR2PCHQs', 'cLpO0U3p97c', 'tKdJHWo-kLI', 'ecKEnrWIh7Q', 'UAHP1VgljnE', '5f2AFS6PgEs', 'rhrFqwPYwig', 'scXuReCe2Co', '_ThBN0zMM9g', 'B48V42s3dnc'],
        1: ['GRIMTo9Kyrk', 'dOQhvvNHAFk', 'hm33x3jVO70'],
        2: ['6UxLDsT2VTk', 'L3Zyj2HU9tI', 'kmLmsXqL6BI', '8L-MINLlMIc', '39NWW8Q3mIk', 'CTYd-2pWXpM'],
        3: ['F_wfPMaLeXs', 'RaNiHfXCp8A', '36S6frKMXX8', 'vhvU0-TU6Zc', 'eqfFj7OJ1u4'],
        4: ['vQHqAfc6Mjk', '75tay629QyQ', '0189i1ripvE'],
        5: ['SJAjezgTBZw'],
        6: ['53Icr-FluPs', 'BlZ2kw1_xfw', 'v-TBS3qrQhI', '_kcw0ITkOKA', 'xMgicLWUebg', '0N2qS-O-uxo', 'EvW2Rjjyxn0', 'JX_oH8amzOI', 'b7fkx4VZuXg', 'l8nngQsCOc0', 'BHb-B0XEF14', 'hYuDceLh69g', '-d5xM1C1tlo', 'KnsIQFrPWHw', 'LNhB9uZnIBw', 'J2fclJEcGXQ', 'C_q2duwuPFw', '-Rc-6VMKydA', '5i19X5bPHNI', 'jyzo8G6yMAc', 'gHcCZzk4pxk', 'uR2h1hCJ-zg', 'hWCQcQqTLhg', 'Smzcq1E6bDU'],
        7: ['gRAjH-FSofA', 'K4tgU1JN6P8', 'fhcY68lCQNU', '9zX6fljTfEw'],
        8: ['YD5QQLhhCyQ', '8iaJA_Fs_w8', 'cFc99sHqBTU', 'jF7tuqxE0Gs', 'dthmyYUi7Es', 'z32h2JUiGzA', 'dVUJN3n4ePk', 'v5Xff5p4VcM', 'yMvy2JGGvxw', 'ed0CcFcBBMI', '70HO9Ga6IAY', '75tay629QyQ', 'hAopzWKVdX4', 'EYQJ1jnP-I8', 'css1gXopHfg', 'xkytDbjvi0c', '7Vwc2o6is6o', 'W50T9G-O7gU', 'JRgUXhQqO3w', 'nj9xmK11vPs', '8M80_logcOQ', 'RYK2Rrysqeg'],
        9: ['Le85YH7K_mE', '81kzxCNBKM4', '_EfRa_ywkEw', 'TFRPcnw_oqY', '6FyN34oVD-w', '2zHjtH-6Oho', 'KIVP4USaVJk', 'jXaHDtZSR70', 'ZSat_xY9pcU', 'zV8HByBA3_8', '0mCQxNXT8A4', 'krIHTd-7PGY', 'ZvtzcQJaYJQ', '5u84jGWJxj0', 'VxwprP-O0So', '3OJicL9tdOU', 'huWdaVJS8yY', 'pnlZjGlCchA', 'nvhC-sfNqL4', 'ldY9mGCcql4', 'mC57r3dronE', 'VHDvG3bvkW4', 'wcO3ZXm3oSc', 'dOQhvvNHAFk', 'BMlmUnXSDy8', 'MFj42lBdJXU', 'PZynBaYrdpU', 'Gg3EHytbROU', 'JbmxSxxRl9Y', 'abmuyFkCka0', 'y0vcpL6GnyE'],
        10: ['IDD5_z3kKCU'],
        11: ['8ysfAJZlqWE', 'jukpx3vpRG4', '-K8sOQMbt2Y', 'WOGAwenS9oQ', 'fi7sBXorcC4', 'FMO377gw8F8', 'Ap7IAeNC4Ws', 'RlcShLzSLxc', 'MaQiJRMwJEw', 'm0HS45AygzM', 'Q1hOBbSdIYo', 'ATdl1_lyAbI', 'SR-12BXlt88', 'qVy8nB_hT18', 'Ge2oip3tmQA', 'g4YccawSQ1g', 'EXyeamh3Mbw', 'g_8062N5zQs', 'u4wOdsbgbMs', '91pQYxPqK2Q', 'XHHylBt_J74', '4jVJxPLo4Jg', 'LSpINqHE66g', 'oLR7OAaxKaY', 'QKm99bWL3TQ', 'L4TtasY-QTo', 'l6NxV5fcdkg', 'SmTRaSg2fTQ', 'mazPt-kEoUE', 'V1AbF_fnTq0', 'tr-GNtoT810', 'prflhTQah9w', 'qMQMqDp0WRM', 'bIoZgT3z1d0', '_Xfw7J9Hv7E', 'n9svf5QwfE0', 'sLl2Bx-aerA'],
        12: ['aFLVzk-12Zk', '5yIFrqY8JHk', 'GjgZkEBZ-LE', 'OaOeMJnFTPU', '2n38FXtnv7Q', '3L23oeGRWgQ', 'CDgxtFjjI2w', '0KvNmjYU7fY', 'UOHy5Sc0gTs', 'OzSs_Zj3VrM', 'Wtuxke576mo', '8hGp4HRS-i8', 'djQRh-RjILo', 'bhT59fGmjms', 'K8DFpdCkdns', 'VMJS2aIpFtQ', '6gb9aV7nG_g', 'vrybNsmdg2Q', 'jM6WLmFNlYg', 'h1tTGsPp7kY', '3UlDGZAHU4Y', 'QkAyVvtApKs'],
        13: ['ta_4hBWwlXU', 'teXv84f56TI', 'XJF5GaZ_GBU', '7_lopC6G_yk', '3EFUbX0RKY4', 'j5ZUbKz7cPQ'],
        14: ['gR37CrZT-kY', 'JkXu2yE199g', '5U3gX9Qk4yk', '1pi92Bbi4DQ', 'nddpbzfX8CQ', 'w5cbKQdFY44', 'SiD0WinCeIo', '8AGToyVpTXA'],
        15: ['jbK68mHsLfg', '98jt_U0jJ7E', 'g5tA599ejgI', 'vdZ6SW6CXCQ', 'zZN7Q9wg7-E', '92f_BNFNHNw', '3f5NfQV8s7o', 'USdGpAfazcg', 'p735iJXDVTI', '40C_kbazS4k', '0mCQxNXT8A4', 'hqvE4Xwc3ts', 'GqNmImL-dgw', '2J8IUUtmLE0', 'E2k-at-JWHw', 'OJFu4STrVH0', 'jQW3StI6fmQ', 'zPVA2J_8Rp0', 'rdLk2QBzvtc', '4UHcxwgifkA', 'DKNXjcJ9k6A', 'eAngyUowXvg'],
        16: ['FhbCZ51HM8E', 'NAKsWDdxo5k', '1gABYdLOQpY', 'kFkp8JrkPsQ', 'nAtTxQTMHAo', 'A3ETK4WJvVo', 'rnidk5D8zXg', 'nt8kA3_5Igc', '32PKh_5GPnI', 'W5dzCop4tzU'],
        17: ['hEWfJLMvx1A'],
        18: ['TT9JkgZoiuY', 'nx59bl-BB1o', 'ADi66Vt5jK8', 'NEpZoGoQEUk', 'xxFK3evO7p8', 'l2bLKltY8Lo', '4uq8r6Czxl0', 'cj4AX1KLHVg', 'oCqpdihI0_4', 'kp573-v625Y', '1tJhYWaHyhE', 'lVdi1jaTxlc', 'H52OZEXtEnQ', 'pt_rU-ZC_7o', 'ecgp5SZgKHU', 'm32duJnYsvI', 'u-CCHDQVzr4', '34FubFtNC5g', 'tXWVFXkMhcE', 'n8n1YUVF7IA', 'vrybNsmdg2Q', 'mdskEOdONAg', 'LZ_WlubEQc0', 'zPVA2J_8Rp0', 'ZuGf78HgZRE', 'Hc4utd--utk'],
        19: ['2Td_w5WXYnI', 'ZRUiNvCMgc4', 'yFLA3AotTHk', 'GptkdoVohr4', 'lcFQqLrgPpA', 'UO3RLLoWGLA'],
        20: ['4a5yL9Bc4_o', '26V04Q5_jJQ', 'A76AhZxOV_c', 'PW6Gps7J-DM', 'xQSTdR3Po28', '9ygI-ARlYVI', '79y4Ld2_yt8', 'DZ6A7YAzAZA', '1W0OA_l9LiQ', 'HAaTY6BrIGg', 'A0yntW5zRg8', 'dGbV6VUvsFU'],
        21: ['uUwiFtXsh7Q', 'CIu2g17Bubk', 'H52OZEXtEnQ', '1Oi12PBSlgk', 'YlKY4EImAWM', 'wD3l5vONVR0', '3OWljFqxfgY', 'pt13BTQ4smE', '9s5s7QuAYsk', 'nDRz01TrjgY', 'TJ5x_tDgrZE', 'lWY-5oeLTL4', 'K5IdTqP70Us', '3auRYESQkGw'],
        22: ['XI3O0qO_XyY', 'AAf8cME5STM', 'iITAUEE9Ja0', 'zRc5o3NXHE4', '9VyK8M5gNt0', 'aFLVzk-12Zk', 'EXRjvh3-NFs', 'izunivHWztc', '4L0lylBK8gE', 'fNrF4v9MfIg', '2n38FXtnv7Q', '0kgii7qQwWQ', 'QbjNWULcdwI', 'wlbDK3PHcLI', 'u4wOdsbgbMs', 'QK3Q6igbvhA', '3sqRS_wqwBQ', 'vYRCBrY5KNk', 'e9FDun2_j7Y', '0aPgAMC_xLw', '5H6woZUYeHQ', 'ZjqInVMdzQY', '9CZaYE0pBNs', 'duCMwFOKtiE', 'hl16iyDGa6E', 'iONBZvzaFso', 'TcUYr4iokTg', '4UHcxwgifkA', 'TfyUUvhb_vs', 'xz4eOlHJS60', 'UmXwB1jiWD8'],
        23: ['Emgq96oOKPw']
    }
    
    for playlist in playlist_dic:
        if playlist == tag:
            playlist_get = playlist_dic[tag]

    return playlist_get


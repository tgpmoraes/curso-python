from numpy import NAN

banking_columns = ['cust_id', 'acct_amount', 'acct_cur', 'inv_amount', 'account_opened', 'last_transaction']

banking_values = [['8C35540A', 44244.71, 'dollar', 35500.5, '03-05-18', '30-09-19'],
 ['D5536652', 86506.85, 'dollar', 81921.86, '21-01-18', '14-01-19'],
 ['A631984D', 77799.33, 'dollar', 46412.27, '26-01-18', '06-10-19'],
 ['93F2F951', 103262.76400000001, 'dollar', 76563.35, '21-08-17', '10-07-19'],
 ['DE0A0882', 109998.18500000001, 'dollar', 18669.01, '05-06-17', '15-01-19'],
 ['25E68E1B', 109737.62, 'dollar', 93552.69, '26-12-17', '12-11-18'],
 ['3FA9296D', 79744.23, 'dollar', 70357.7, '21-06-18', '24-08-18'],
 ['984403B9', 19733.868000000002, 'dollar', 14429.59, '07-10-17', '18-05-18'],
 ['870A9281', 63523.31, 'dollar', 51297.32, '02-09-18', '22-02-19'],
 ['166B05B0', 41993.006, 'dollar', 15052.7, '28-02-19', '31-10-18'],
 ['0A9BA907', 90469.53, 'dollar', 70173.49, '15-06-18', '28-08-18'],
 ['2AB6539A', 53796.13, 'dollar', 12401.32, '03-01-19', '17-11-18'],
 ['F389832C', 95380.06, 'dollar', 58388.14, '03-02-18', '23-09-18'],
 ['9A9BB390', 92018.399, 'dollar', 44656.36, '15-08-18', '18-01-19'],
 ['E7389E60', 86028.48, 'dollar', 48086.69, '04-06-17', '07-08-18'],
 ['CA507BA1', 12209.84, 'dollar', 7516.33, '26-05-18', '11-09-19'],
 ['472341F2', 91440.41500000001, 'dollar', 67961.74, '14-12-18', '22-04-18'],
 ['D3287768', 98957.94700000001, 'dollar', 84216.09, '03-09-18', '19-10-18'],
 ['FA01676F', 66947.3, 'dollar', 52551.65, '10-08-18', '23-07-19'],
 ['A69FA1B8', 82728.78900000002, 'dollar', 31620.86, '23-02-19', '09-09-19'],
 ['9B550FD5', 32891.31, 'dollar', 11993.35, '02-05-18', '27-06-19'],
 ['B99CD662', 92838.44, 'dollar', 49090.83, '04-05-17', '12-03-19'],
 ['7A73F334', 132563.2, 'dollar', 93233.0, '14-05-18', '19-07-18'],
 ['B40E8497', 109749.09, 'dollar', 86992.74, '16-05-17', '05-01-20'],
 ['1B55AA1C', 78960.42, 'dollar', 35476.83, '29-01-19', '22-11-19'],
 ['68C55974', 95038.14, 'dollar', 66797.81, '03-04-18', '25-09-18'],
 ['EC189A55', 83343.18, 'dollar', 7282.91, '04-02-19', '31-12-18'],
 ['3C5CBBD7', 65645.811, 'dollar', 35939.08, '03-01-19', '02-10-18'],
 ['F7FC8F78', 88049.82, 'dollar', 84432.03, '28-02-18', '30-04-18'],
 ['ACE5C956', 90413.25, 'dollar', 21574.21, '29-12-18', '30-04-19'],
 ['2EC1B555', 55976.78, 'dollar', 51478.91, '05-12-17', '21-10-19'],
 ['B6F69B7A', 92007.12, 'dollar', 22053.26, '29-07-18', '10-02-20'],
 ['5321D380', 59700.08, 'dollar', 8145.24, '09-10-18', '04-02-19'],
 ['C55C54A8', 79630.02, 'dollar', 25250.82, '30-10-18', '19-02-19'],
 ['AC2AEAC4', 88440.54, 'dollar', 63332.9, '12-03-18', '01-08-19'],
 ['904A19DD', 31981.36, 'dollar', 13189.63, '28-01-19', '23-06-19'],
 ['A731C34E', 95352.02, 'dollar', 84066.66, '13-11-17', '13-01-19'],
 ['96525DA6', 90762.36400000002, 'dollar', 33929.23, '23-07-18', '07-08-18'],
 ['BD7CF5D7', 90293.236, 'dollar', 44340.56, '18-07-17', '26-02-20'],
 ['0109137B', 31730.19, 'dollar', 21959.28, '20-04-18', '08-07-19'],
 ['93E78DA3', 41942.23, 'dollar', 29663.88, '09-10-17', '15-04-18'],
 ['72DD1471', 100683.48, 'dollar', 87882.91, '22-01-18', '17-05-18'],
 ['EC7C25A8', 86503.33, 'dollar', 49180.36, '08-06-17', '02-04-18'],
 ['38B8CD9C', 28834.71, 'dollar', 27532.35, '17-09-18', '05-02-20'],
 ['80C0DAB3', 81346.595, 'dollar', 61650.12, '03-04-17', '21-09-19'],
 ['DEC6DBE4', 32220.83, 'dollar', 3216.72, '09-08-18', '17-11-19'],
 ['3B240FEF', 97856.46, 'dollar', 64839.79, '23-05-18', '11-10-18'],
 ['82E87321', 97833.54, 'dollar', 61481.86, '18-10-18', '21-07-18'],
 ['1903EB99', 26693.722, 'dollar', 22963.63, '17-03-17', '21-11-18'],
 ['2F4F99C1', 82058.48, 'dollar', 35760.69, '30-12-18', '11-08-18'],
 ['46351200', 97595.3, 'dollar', 82251.59, '18-08-18', '20-02-20'],
 ['7D8EBAF6', 120937.33300000001, 'dollar', 81490.13, '02-07-17', '22-02-20'],
 ['E2EFF324', 74027.20600000002, 'dollar', 57252.76, '27-04-18', '10-07-18'],
 ['A1815565', 91295.644, 'dollar', 30898.16, '07-11-17', '30-09-19'],
 ['6B094617', 98841.57800000001, 'dollar', 34551.43, '06-02-18', '14-02-19'],
 ['C580AE41', 96673.37, 'dollar', 68468.28, '28-09-18', '17-09-18'],
 ['B25B3B8D', 99193.98, 'dollar', 83364.21, '28-04-18', '04-07-19'],
 ['0F0884F6', 84505.81, 'dollar', 47826.51, '08-03-18', '24-08-19'],
 ['58F8CC80', 87146.19, 'dollar', 25759.85, '18-10-18', '10-01-19'],
 ['56D310A8', 88660.4, 'dollar', 62307.9, '25-02-18', '29-07-18'],
 ['4A13E345', 84107.71, 'dollar', 4217.92, '17-09-18', '09-02-19'],
 ['5AEA5AB8', 100266.99, 'dollar', 89342.43, '09-06-18', '03-07-19'],
 ['7A4EED75', 98923.14, 'dollar', 20932.3, '28-11-17', '01-05-19'],
 ['19C86773', 63182.57, 'dollar', 62692.03, '09-05-18', '26-01-20'],
 ['87FDF627', 95275.46, 'dollar', 55888.87, '26-02-19', '25-06-18'],
 ['FBAD3C91', 99141.9, 'dollar', 13468.4, '29-05-18', '02-11-19'],
 ['BFC13E88', 65850.147, 'dollar', 24569.47, '25-04-18', '02-04-18'],
 ['5F6A2443', 98047.16, 'dollar', 76216.88, '15-12-18', '12-11-19'],
 ['7A2879AF', 83345.15, 'dollar', 45162.06, '30-08-18', '09-11-19'],
 ['13770971', 92750.87, 'dollar', 27963.45, '16-08-17', '24-04-19'],
 ['EC10469C', 80980.625, 'dollar', 48979.16, '27-12-18', '08-06-18'],
 ['B5D367B5', 44226.86, 'dollar', 36572.69, '16-09-17', '03-04-19'],
 ['AC91D689', 99490.61, 'dollar', 32150.64, '01-08-17', '04-08-19'],
 ['625167AC', 95315.71, 'dollar', 66914.63, '08-06-17', '03-07-19'],
 ['777A7F2C', 52684.17, 'dollar', 20970.35, '27-10-18', '25-05-19'],
 ['3E51A395', 21757.14, 'dollar', 10582.94, '04-06-17', '22-09-18'],
 ['2C5901B4', 275051.43600000005, 'dollar', 90442.57, '05-02-18', '11-07-19'],
 ['D4C7E817', 26585.87, 'dollar', 20441.92, '06-05-18', '08-12-18'],
 ['DEB87C87', 71439.08200000001, 'dollar', 31803.34, '20-03-18', '15-11-19'],
 ['E52D4C7F', 67975.479, 'dollar', 49387.29, '22-05-17', '24-10-19'],
 ['987DC93E', 39516.85100000001, 'dollar', 14881.89, '30-12-18', '06-12-18'],
 ['A07D5C92', 99577.36, 'dollar', 60408.99, '17-11-17', '16-01-20'],
 ['078C654F', 87312.64, 'dollar', 66531.16, '14-04-17', '05-08-18'],
 ['807465A4', 28827.59, 'dollar', 14585.75, '20-04-17', '31-07-18'],
 ['8D08495A', 89138.52, 'dollar', 60798.23, '08-08-18', '05-02-19'],
 ['C9FB0E86', 97550.57400000001, 'dollar', 26166.11, '19-05-18', '06-08-19'],
 ['296A9395', 38147.560000000005, 'dollar', 28459.96, '24-12-17', '19-02-19'],
 ['F2158F66', 92545.31000000001, 'dollar', 23714.06, '07-11-17', '08-11-18'],
 ['33CA2B76', 75508.61, 'dollar', 27008.2, '16-11-17', '03-03-19'],
 ['EEBD980F', 63622.339, 'dollar', 50814.83, '08-12-18', '04-01-20'],
 ['014E0511', 70272.97, 'dollar', 65969.8, '09-02-19', '22-05-19'],
 ['0B44C3F8', 33984.87, 'dollar', 31395.0, '10-04-18', '28-09-19'],
 ['CEC1CAE5', 92169.14, 'dollar', 77896.86, '26-11-17', '08-10-18'],
 ['4C7F8638', 21942.37, 'dollar', 11715.24, '14-07-18', '02-02-19'],
 ['A81D31B3', 74010.15, 'dollar', 48787.47, '02-06-18', '12-09-18'],
 ['93A17007', 40651.36, 'dollar', 9387.87, '28-05-17', '08-03-19'],
 ['E961CA44', 27907.16, 'dollar', 10967.69, '23-10-17', '11-07-19']]

banking_missing_columns = ['cust_id', 'age', 'acct_amount', 'inv_amount', 'account_opened', 'last_transaction']

banking_missing_values = [['8C35540A', 54, 44244.71, 35500.5, '03-05-18', '30-09-19'],
 ['D5536652', 36, 86506.85, 81921.86, '21-01-18', '14-01-19'],
 ['A631984D', 49, 77799.33, 46412.27, '26-01-18', '06-10-19'],
 ['93F2F951', 56, 93875.24, 76563.35, '21-08-17', '10-07-19'],
 ['DE0A0882', 21, 99998.35, NAN, '05-06-17', '15-01-19'],
 ['25E68E1B', 47, 109737.62, 93552.69, '26-12-17', '12-11-18'],
 ['3FA9296D', 53, 79744.23, 70357.7, '21-06-18', '24-08-18'],
 ['984403B9', 29, 17939.88, 14429.59, '07-10-17', '18-05-18'],
 ['870A9281', 58, 63523.31, 51297.32, '02-09-18', '22-02-19'],
 ['166B05B0', 53, 38175.46, 15052.7, '28-02-19', '31-10-18'],
 ['0A9BA907', 44, 90469.53, 70173.49, '15-06-18', '28-08-18'],
 ['2AB6539A', 59, 53796.13, 12401.32, '03-01-19', '17-11-18'],
 ['F389832C', 48, 95380.06, 58388.14, '03-02-18', '23-09-18'],
 ['9A9BB390', 34, 83653.09, 44656.36, '15-08-18', '18-01-19'],
 ['E7389E60', 22, 86028.48, NAN, '04-06-17', '07-08-18'],
 ['CA507BA1', 50, 12209.84, 7516.33, '26-05-18', '11-09-19'],
 ['472341F2', 35, 83127.65, 67961.74, '14-12-18', '22-04-18'],
 ['D3287768', 20, 89961.77, NAN, '03-09-18', '19-10-18'],
 ['FA01676F', 21, 66947.3, NAN, '10-08-18', '23-07-19'],
 ['A69FA1B8', 41, 75207.99, 31620.86, '23-02-19', '09-09-19'],
 ['9B550FD5', 42, 32891.31, 11993.35, '02-05-18', '27-06-19'],
 ['B99CD662', 28, 92838.44, 49090.83, '04-05-17', '12-03-19'],
 ['7A73F334', 35, 120512.0, 93233.0, '14-05-18', '19-07-18'],
 ['B40E8497', 33, 99771.9, 86992.74, '16-05-17', '05-01-20'],
 ['1B55AA1C', 30, 71782.2, 35476.83, '29-01-19', '22-11-19'],
 ['68C55974', 50, 95038.14, 66797.81, '03-04-18', '25-09-18'],
 ['EC189A55', 53, 83343.18, 7282.91, '04-02-19', '31-12-18'],
 ['3C5CBBD7', 45, 59678.01, 35939.08, '03-01-19', '02-10-18'],
 ['F7FC8F78', 26, 88049.82, 84432.03, '28-02-18', '30-04-18'],
 ['ACE5C956', 39, 90413.25, 21574.21, '29-12-18', '30-04-19'],
 ['2EC1B555', 34, 55976.78, 51478.91, '05-12-17', '21-10-19'],
 ['B6F69B7A', 43, 92007.12, 22053.26, '29-07-18', '10-02-20'],
 ['5321D380', 58, 59700.08, 8145.24, '09-10-18', '04-02-19'],
 ['C55C54A8', 45, 79630.02, 25250.82, '30-10-18', '19-02-19'],
 ['AC2AEAC4', 57, 88440.54, 63332.9, '12-03-18', '01-08-19'],
 ['904A19DD', 20, 31981.36, NAN, '28-01-19', '23-06-19'],
 ['A731C34E', 46, 95352.02, 84066.66, '13-11-17', '13-01-19'],
 ['96525DA6', 33, 82511.24, 33929.23, '23-07-18', '07-08-18'],
 ['BD7CF5D7', 29, 82084.76, 44340.56, '18-07-17', '26-02-20'],
 ['0109137B', 44, 31730.19, 21959.28, '20-04-18', '08-07-19'],
 ['93E78DA3', 22, 41942.23, NAN, '09-10-17', '15-04-18'],
 ['72DD1471', 27, 100683.48, 87882.91, '22-01-18', '17-05-18'],
 ['EC7C25A8', 30, 86503.33, 49180.36, '08-06-17', '02-04-18'],
 ['38B8CD9C', 55, 28834.71, 27532.35, '17-09-18', '05-02-20'],
 ['80C0DAB3', 27, 73951.45, 61650.12, '03-04-17', '21-09-19'],
 ['DEC6DBE4', 46, 32220.83, 3216.72, '09-08-18', '17-11-19'],
 ['3B240FEF', 25, 97856.46, NAN, '23-05-18', '11-10-18'],
 ['82E87321', 50, 97833.54, 61481.86, '18-10-18', '21-07-18'],
 ['1903EB99', 37, 24267.02, 22963.63, '17-03-17', '21-11-18'],
 ['2F4F99C1', 53, 82058.48, 35760.69, '30-12-18', '11-08-18'],
 ['46351200', 56, 97595.3, 82251.59, '18-08-18', '20-02-20'],
 ['7D8EBAF6', 52, 109943.03, 81490.13, '02-07-17', '22-02-20'],
 ['E2EFF324', 29, 67297.46, 57252.76, '27-04-18', '10-07-18'],
 ['A1815565', 32, 82996.04, 30898.16, '07-11-17', '30-09-19'],
 ['6B094617', 21, 89855.98, NAN, '06-02-18', '14-02-19'],
 ['C580AE41', 47, 96673.37, 68468.28, '28-09-18', '17-09-18'],
 ['B25B3B8D', 57, 99193.98, 83364.21, '28-04-18', '04-07-19'],
 ['0F0884F6', 56, 84505.81, 47826.51, '08-03-18', '24-08-19'],
 ['58F8CC80', 42, 87146.19, 25759.85, '18-10-18', '10-01-19'],
 ['56D310A8', 21, 88660.4, NAN, '25-02-18', '29-07-18'],
 ['4A13E345', 45, 84107.71, 4217.92, '17-09-18', '09-02-19'],
 ['5AEA5AB8', 56, 100266.99, 89342.43, '09-06-18', '03-07-19'],
 ['7A4EED75', 33, 98923.14, 20932.3, '28-11-17', '01-05-19'],
 ['19C86773', 49, 63182.57, 62692.03, '09-05-18', '26-01-20'],
 ['87FDF627', 56, 95275.46, 55888.87, '26-02-19', '25-06-18'],
 ['FBAD3C91', 35, 99141.9, 13468.4, '29-05-18', '02-11-19'],
 ['BFC13E88', 58, 59863.77, 24569.47, '25-04-18', '02-04-18'],
 ['5F6A2443', 57, 98047.16, 76216.88, '15-12-18', '12-11-19'],
 ['7A2879AF', 54, 83345.15, 45162.06, '30-08-18', '09-11-19'],
 ['13770971', 26, 92750.87, 27963.45, '16-08-17', '24-04-19'],
 ['EC10469C', 28, 73618.75, 48979.16, '27-12-18', '08-06-18'],
 ['B5D367B5', 39, 44226.86, 36572.69, '16-09-17', '03-04-19'],
 ['AC91D689', 53, 99490.61, 32150.64, '01-08-17', '04-08-19'],
 ['625167AC', 28, 95315.71, 66914.63, '08-06-17', '03-07-19'],
 ['777A7F2C', 30, 52684.17, 20970.35, '27-10-18', '25-05-19'],
 ['3E51A395', 46, 21757.14, 10582.94, '04-06-17', '22-09-18'],
 ['2C5901B4', 40, 250046.76, 90442.57, '05-02-18', '11-07-19'],
 ['D4C7E817', 56, 26585.87, 20441.92, '06-05-18', '08-12-18'],
 ['DEB87C87', 41, 64944.62, 31803.34, '20-03-18', '15-11-19'],
 ['E52D4C7F', 36, 61795.89, 49387.29, '22-05-17', '24-10-19'],
 ['987DC93E', 51, 35924.41, 14881.89, '30-12-18', '06-12-18'],
 ['A07D5C92', 45, 99577.36, 60408.99, '17-11-17', '16-01-20'],
 ['078C654F', 21, 87312.64, NAN, '14-04-17', '05-08-18'],
 ['807465A4', 48, 28827.59, 14585.75, '20-04-17', '31-07-18'],
 ['8D08495A', 59, 89138.52, 60798.23, '08-08-18', '05-02-19'],
 ['C9FB0E86', 46, 88682.34, 26166.11, '19-05-18', '06-08-19'],
 ['296A9395', 48, 34679.6, 28459.96, '24-12-17', '19-02-19'],
 ['F2158F66', 41, 84132.1, 23714.06, '07-11-17', '08-11-18'],
 ['33CA2B76', 23, 75508.61, NAN, '16-11-17', '03-03-19'],
 ['EEBD980F', 59, 57838.49, 50814.83, '08-12-18', '04-01-20'],
 ['014E0511', 27, 70272.97, 65969.8, '09-02-19', '22-05-19'],
 ['0B44C3F8', 32, 33984.87, 31395.0, '10-04-18', '28-09-19'],
 ['CEC1CAE5', 32, 92169.14, 77896.86, '26-11-17', '08-10-18'],
 ['4C7F8638', 23, 21942.37, NAN, '14-07-18', '02-02-19'],
 ['A81D31B3', 24, 74010.15, NAN, '02-06-18', '12-09-18'],
 ['93A17007', 36, 40651.36, 9387.87, '28-05-17', '08-03-19'],
 ['E961CA44', 57, 27907.16, 10967.69, '23-10-17', '11-07-19']]

banking_missing_columns2 = ['cust_id', 'acct_amount', 'inv_amount', 'account_opened', 'last_transaction']

banking_missing_values2 = [['8C35540A', 44244.71, 35500.5, '03-05-18', '30-09-19'],
 ['D5536652', NAN, 81921.86, '21-01-18', '14-01-19'],
 ['A631984D', NAN, 46412.27, '26-01-18', '06-10-19'],
 ['93F2F951', NAN, 76563.35, '21-08-17', '10-07-19'],
 ['DE0A0882', NAN, 18669.01, '05-06-17', '15-01-19'],
 ['25E68E1B', 109737.62, 93552.69, '26-12-17', '12-11-18'],
 ['3FA9296D', NAN, 70357.7, '21-06-18', '24-08-18'],
 ['984403B9', NAN, 14429.59, '07-10-17', '18-05-18'],
 ['870A9281', 63523.31, 51297.32, '02-09-18', '22-02-19'],
 ['166B05B0', 38175.46, 15052.7, '28-02-19', '31-10-18'],
 ['0A9BA907', 90469.53, 70173.49, '15-06-18', '28-08-18'],
 ['2AB6539A', 53796.13, 12401.32, '03-01-19', '17-11-18'],
 ['F389832C', NAN, 58388.14, '03-02-18', '23-09-18'],
 [NAN, 83653.09, 44656.36, '15-08-18', '18-01-19'],
 [NAN, 86028.48, 48086.69, '04-06-17', '07-08-18'],
 ['CA507BA1', 12209.84, 7516.33, '26-05-18', '11-09-19'],
 ['472341F2', 83127.65, 67961.74, '14-12-18', '22-04-18'],
 ['D3287768', 89961.77, 84216.09, '03-09-18', '19-10-18'],
 ['FA01676F', 66947.3, 52551.65, '10-08-18', '23-07-19'],
 ['A69FA1B8', 75207.99, 31620.86, '23-02-19', '09-09-19'],
 ['9B550FD5', 32891.31, 11993.35, '02-05-18', '27-06-19'],
 ['B99CD662', 92838.44, 49090.83, '04-05-17', '12-03-19'],
 ['7A73F334', 120512.0, 93233.0, '14-05-18', '19-07-18'],
 ['B40E8497', 99771.9, 86992.74, '16-05-17', '05-01-20'],
 [NAN, 71782.2, 35476.83, '29-01-19', '22-11-19'],
 [NAN, 95038.14, 66797.81, '03-04-18', '25-09-18'],
 ['EC189A55', 83343.18, 7282.91, '04-02-19', '31-12-18'],
 ['3C5CBBD7', 59678.01, 35939.08, '03-01-19', '02-10-18'],
 ['F7FC8F78', NAN, 84432.03, '28-02-18', '30-04-18'],
 ['ACE5C956', NAN, 21574.21, '29-12-18', '30-04-19'],
 ['2EC1B555', 55976.78, 51478.91, '05-12-17', '21-10-19'],
 [NAN, 92007.12, 22053.26, '29-07-18', '10-02-20'],
 ['5321D380', 59700.08, 8145.24, '09-10-18', '04-02-19'],
 ['C55C54A8', 79630.02, 25250.82, '30-10-18', '19-02-19'],
 ['AC2AEAC4', 88440.54, 63332.9, '12-03-18', '01-08-19'],
 ['904A19DD', 31981.36, 13189.63, '28-01-19', '23-06-19'],
 ['A731C34E', 95352.02, 84066.66, '13-11-17', '13-01-19'],
 ['96525DA6', 82511.24, 33929.23, '23-07-18', '07-08-18'],
 ['BD7CF5D7', 82084.76, 44340.56, '18-07-17', '26-02-20'],
 ['0109137B', 31730.19, 21959.28, '20-04-18', '08-07-19'],
 ['93E78DA3', 41942.23, 29663.88, '09-10-17', '15-04-18'],
 ['72DD1471', NAN, 87882.91, '22-01-18', '17-05-18'],
 ['EC7C25A8', 86503.33, 49180.36, '08-06-17', '02-04-18'],
 ['38B8CD9C', 28834.71, 27532.35, '17-09-18', '05-02-20'],
 ['80C0DAB3', NAN, 61650.12, '03-04-17', '21-09-19'],
 ['DEC6DBE4', 32220.83, 3216.72, '09-08-18', '17-11-19'],
 ['3B240FEF', 97856.46, 64839.79, '23-05-18', '11-10-18'],
 ['82E87321', 97833.54, 61481.86, '18-10-18', '21-07-18'],
 ['1903EB99', 24267.02, 22963.63, '17-03-17', '21-11-18'],
 ['2F4F99C1', 82058.48, 35760.69, '30-12-18', '11-08-18'],
 ['46351200', NAN, 82251.59, '18-08-18', '20-02-20'],
 ['7D8EBAF6', 109943.03, 81490.13, '02-07-17', '22-02-20'],
 ['E2EFF324', 67297.46, 57252.76, '27-04-18', '10-07-18'],
 ['A1815565', 82996.04, 30898.16, '07-11-17', '30-09-19'],
 ['6B094617', 89855.98, 34551.43, '06-02-18', '14-02-19'],
 ['C580AE41', 96673.37, 68468.28, '28-09-18', '17-09-18'],
 ['B25B3B8D', 99193.98, 83364.21, '28-04-18', '04-07-19'],
 ['0F0884F6', 84505.81, 47826.51, '08-03-18', '24-08-19'],
 ['58F8CC80', NAN, 25759.85, '18-10-18', '10-01-19'],
 ['56D310A8', NAN, 62307.9, '25-02-18', '29-07-18'],
 ['4A13E345', 84107.71, 4217.92, '17-09-18', '09-02-19'],
 ['5AEA5AB8', 100266.99, 89342.43, '09-06-18', '03-07-19'],
 ['7A4EED75', 98923.14, 20932.3, '28-11-17', '01-05-19'],
 [NAN, 63182.57, 62692.03, '09-05-18', '26-01-20'],
 ['87FDF627', 95275.46, 55888.87, '26-02-19', '25-06-18'],
 ['FBAD3C91', 99141.9, 13468.4, '29-05-18', '02-11-19'],
 ['BFC13E88', 59863.77, 24569.47, '25-04-18', '02-04-18'],
 ['5F6A2443', 98047.16, 76216.88, '15-12-18', '12-11-19'],
 ['7A2879AF', 83345.15, 45162.06, '30-08-18', '09-11-19'],
 ['13770971', 92750.87, 27963.45, '16-08-17', '24-04-19'],
 ['EC10469C', 73618.75, 48979.16, '27-12-18', '08-06-18'],
 ['B5D367B5', 44226.86, 36572.69, '16-09-17', '03-04-19'],
 [NAN, 99490.61, 32150.64, '01-08-17', '04-08-19'],
 ['625167AC', 95315.71, 66914.63, '08-06-17', '03-07-19'],
 ['777A7F2C', 52684.17, 20970.35, '27-10-18', '25-05-19'],
 ['3E51A395', 21757.14, 10582.94, '04-06-17', '22-09-18'],
 ['2C5901B4', 250046.76, 90442.57, '05-02-18', '11-07-19'],
 ['D4C7E817', 26585.87, 20441.92, '06-05-18', '08-12-18'],
 [NAN, 64944.62, 31803.34, '20-03-18', '15-11-19'],
 ['E52D4C7F', 61795.89, 49387.29, '22-05-17', '24-10-19'],
 ['987DC93E', 35924.41, 14881.89, '30-12-18', '06-12-18'],
 ['A07D5C92', 99577.36, 60408.99, '17-11-17', '16-01-20'],
 ['078C654F', 87312.64, 66531.16, '14-04-17', '05-08-18'],
 ['807465A4', 28827.59, 14585.75, '20-04-17', '31-07-18'],
 ['8D08495A', 89138.52, 60798.23, '08-08-18', '05-02-19'],
 ['C9FB0E86', 88682.34, 26166.11, '19-05-18', '06-08-19'],
 ['296A9395', 34679.6, 28459.96, '24-12-17', '19-02-19'],
 ['F2158F66', 84132.1, 23714.06, '07-11-17', '08-11-18'],
 ['33CA2B76', 75508.61, 27008.2, '16-11-17', '03-03-19'],
 ['EEBD980F', 57838.49, 50814.83, '08-12-18', '04-01-20'],
 ['014E0511', 70272.97, 65969.8, '09-02-19', '22-05-19'],
 ['0B44C3F8', 33984.87, 31395.0, '10-04-18', '28-09-19'],
 ['CEC1CAE5', 92169.14, 77896.86, '26-11-17', '08-10-18'],
 ['4C7F8638', 21942.37, 11715.24, '14-07-18', '02-02-19'],
 ['A81D31B3', 74010.15, 48787.47, '02-06-18', '12-09-18'],
 ['93A17007', 40651.36, 9387.87, '28-05-17', '08-03-19'],
 [NAN, 27907.16, 10967.69, '23-10-17', '11-07-19']]
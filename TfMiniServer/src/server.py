import socket
import json
import matplotlib.pyplot as plot


HOST = "192.168.137.2"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    json_buffer = b''
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            json_buffer += data
            if not data:
                break
    s.close()

json_data = json.loads(json_buffer.decode('utf-8'))
print(json_data)

name = 'three_items_with_line_bounds_trial4'
angles =  [89.80000000000001, 78.00000000000068, 77.90000000000069, 77.6000000000007, 77.50000000000071, 77.20000000000073, 76.70000000000076, 76.50000000000077, 76.40000000000077, 76.30000000000078, 76.20000000000078, 76.10000000000079, 75.70000000000081, 75.50000000000082, 75.30000000000084, 75.20000000000084, 75.10000000000085, 75.00000000000085, 74.90000000000086, 74.80000000000086, 74.70000000000087, 74.60000000000088, 74.50000000000088, 74.40000000000089, 74.30000000000089, 74.2000000000009, 74.1000000000009, 74.00000000000091, 73.90000000000092, 73.80000000000092, 73.70000000000093, 73.60000000000093, 73.50000000000094, 73.40000000000094, 73.30000000000095, 73.20000000000095, 73.10000000000096, 73.00000000000097, 72.90000000000097, 72.80000000000098, 72.70000000000098, 72.60000000000099, 72.500000000001, 72.400000000001, 72.300000000001, 72.20000000000101, 72.10000000000102, 72.00000000000102, 71.90000000000103, 71.80000000000103, 71.70000000000104, 71.60000000000105, 71.50000000000105, 71.40000000000106, 71.30000000000106, 71.20000000000107, 71.10000000000107, 71.00000000000108, 70.90000000000109, 70.80000000000109, 70.7000000000011, 70.6000000000011, 70.50000000000111, 70.40000000000111, 70.30000000000112, 70.20000000000113, 70.00000000000114, 69.90000000000114, 69.70000000000115, 69.60000000000116, 69.50000000000117, 69.40000000000117, 69.20000000000118, 69.10000000000119, 68.9000000000012, 68.8000000000012, 68.70000000000121, 68.60000000000122, 68.50000000000122, 68.30000000000123, 68.20000000000124, 68.00000000000125, 67.90000000000126, 67.70000000000127, 67.60000000000127, 67.50000000000128, 67.40000000000128, 67.30000000000129, 67.2000000000013, 67.1000000000013, 67.00000000000131, 66.90000000000131, 66.80000000000132, 66.70000000000132, 66.60000000000133, 66.50000000000134, 66.40000000000134, 66.30000000000135, 66.20000000000135, 66.10000000000136, 66.00000000000136, 65.90000000000137, 65.80000000000138, 65.70000000000138, 65.60000000000139, 65.50000000000139, 65.4000000000014, 65.3000000000014, 65.20000000000141, 65.10000000000142, 65.00000000000142, 64.90000000000143, 64.80000000000143, 64.70000000000144, 64.60000000000144, 64.50000000000145, 64.40000000000146, 64.30000000000146, 64.20000000000147, 64.10000000000147, 64.00000000000148, 63.90000000000148, 63.800000000001475, 63.700000000001474, 63.60000000000147, 63.50000000000147, 63.40000000000147, 63.30000000000147, 63.20000000000147, 63.100000000001465, 63.000000000001464, 62.90000000000146, 62.80000000000146, 62.70000000000146, 62.60000000000146, 62.50000000000146, 62.400000000001455, 62.300000000001454, 62.20000000000145, 62.10000000000145, 62.00000000000145, 61.90000000000145, 61.80000000000145, 61.700000000001445, 61.600000000001444, 61.50000000000144, 61.40000000000144, 61.30000000000144, 61.20000000000144, 61.10000000000144, 61.000000000001435, 60.900000000001434, 60.80000000000143, 60.70000000000143, 60.60000000000143, 60.50000000000143, 60.40000000000143, 60.300000000001425, 60.200000000001424, 60.10000000000142, 60.00000000000142, 59.90000000000142, 59.80000000000142, 59.70000000000142, 59.600000000001415, 59.500000000001414, 59.40000000000141, 59.30000000000141, 59.20000000000141, 59.10000000000141, 59.00000000000141, 58.900000000001405, 58.800000000001404, 58.7000000000014, 58.6000000000014, 58.5000000000014, 58.4000000000014, 58.3000000000014, 58.200000000001396, 58.100000000001394, 58.00000000000139, 57.90000000000139, 57.80000000000139, 57.70000000000139, 57.60000000000139, 57.500000000001386, 57.400000000001384, 57.30000000000138, 57.20000000000138, 57.10000000000138, 57.00000000000138, 56.90000000000138, 56.800000000001376, 56.700000000001374, 56.60000000000137, 56.50000000000137, 56.40000000000137, 56.30000000000137, 56.20000000000137, 56.100000000001366, 56.000000000001364, 55.90000000000136, 55.80000000000136, 55.70000000000136, 55.60000000000136, 55.50000000000136, 55.400000000001356, 55.300000000001354, 55.20000000000135, 55.10000000000135, 55.00000000000135, 54.90000000000135, 54.80000000000135, 54.700000000001346, 54.600000000001344, 54.50000000000134, 54.40000000000134, 54.30000000000134, 54.20000000000134, 54.10000000000134, 54.000000000001336, 53.900000000001334, 53.80000000000133, 53.70000000000133, 53.60000000000133, 53.50000000000133, 53.40000000000133, 53.300000000001326, 53.200000000001324, 53.10000000000132, 53.00000000000132, 52.90000000000132, 52.80000000000132, 52.70000000000132, 52.600000000001316, 52.500000000001315, 52.40000000000131, 52.30000000000131, 52.20000000000131, 52.10000000000131, 52.00000000000131, 51.900000000001306, 51.800000000001305, 51.7000000000013, 51.6000000000013, 51.5000000000013, 51.4000000000013, 51.3000000000013, 51.200000000001296, 51.100000000001295, 51.00000000000129, 50.90000000000129, 50.80000000000129, 50.70000000000129, 50.60000000000129, 50.500000000001286, 50.400000000001285, 50.30000000000128, 50.20000000000128, 50.10000000000128, 50.00000000000128, 49.90000000000128, 49.800000000001276, 49.700000000001275, 49.60000000000127, 49.50000000000127, 49.40000000000127, 49.30000000000127, 49.20000000000127, 49.100000000001266, 49.000000000001265, 48.90000000000126, 48.80000000000126, 48.70000000000126, 48.60000000000126, 48.50000000000126, 48.400000000001256, 48.300000000001255, 48.20000000000125, 48.10000000000125, 48.00000000000125, 47.90000000000125, 47.80000000000125, 47.700000000001246, 47.600000000001245, 47.50000000000124, 47.40000000000124, 47.30000000000124, 47.20000000000124, 47.10000000000124, 47.000000000001236, 46.900000000001235, 46.80000000000123, 46.70000000000123, 46.60000000000123, 46.50000000000123, 46.40000000000123, 46.300000000001226, 46.200000000001225, 46.100000000001224, 46.00000000000122, 45.90000000000122, 45.80000000000122, 45.70000000000122, 45.60000000000122, 45.500000000001215, 45.400000000001214, 45.30000000000121, 45.20000000000121, 45.10000000000121, 45.00000000000121, 44.90000000000121, 44.800000000001205, 44.700000000001204, 44.6000000000012, 44.5000000000012, 44.4000000000012, 44.3000000000012, 44.2000000000012, 44.100000000001195, 44.000000000001194, 43.90000000000119, 43.80000000000119, 43.70000000000119, 43.60000000000119, 43.50000000000119, 43.400000000001185, 43.300000000001184, 43.20000000000118, 43.10000000000118, 43.00000000000118, 42.90000000000118, 42.80000000000118, 42.700000000001175, 42.600000000001174, 42.50000000000117, 42.40000000000117, 42.30000000000117, 42.20000000000117, 42.10000000000117, 42.000000000001165, 41.900000000001164, 41.80000000000116, 41.70000000000116, 41.60000000000116, 41.50000000000116, 41.40000000000116, 41.300000000001155, 41.200000000001154, 41.10000000000115, 41.00000000000115, 40.90000000000115, 40.80000000000115, 40.70000000000115, 40.600000000001145, 40.500000000001144, 40.40000000000114, 40.30000000000114, 40.20000000000114, 40.10000000000114, 40.00000000000114, 39.900000000001135, 39.800000000001134, 39.70000000000113, 39.60000000000113, 39.50000000000113, 39.40000000000113, 39.30000000000113, 39.100000000001124, 39.00000000000112]
distances =  [62.999616182440796, 90.96772686824416, 91.91162425530922, 41.020235690035165, 48.8148003559968, 76.06164963583416, 0.0, 29.17109761193039, 24.299025014463734, 18.459433279955338, 23.307222717831344, 24.26791203945485, 15.504251702509968, 16.458509886427894, 26.116229324948772, 23.203761326507117, 22.226649824390663, 24.148145657226806, 7.723781047033832, 24.125412361807886, 16.397476113782634, 18.31781268044817, 18.308978610963916, 17.336926202357922, 19.25383492852966, 17.319923883527213, 16.349602262336667, 16.341448830951496, 16.333245620679175, 16.32499265650811, 18.236300547528636, 24.942163338041613, 24.92931310657314, 23.95806436162845, 25.86120736082363, 27.76226542843009, 28.70440752172837, 27.732837922928173, 28.673790443950054, 27.703072501548114, 30.552345584089682, 27.672969526972178, 27.65779157169873, 28.595720033788567, 26.674521475100565, 28.563881782264325, 30.4510209241422, 28.531695488854773, 28.51547194883368, 30.39910564878906, 28.482764329257286, 28.46628034933507, 28.44970965618615, 29.38082071029734, 28.416308332381043, 29.346127063586774, 29.328646123654092, 29.31107584357901, 29.29341627688365, 30.220043847599594, 29.25782949908031, 30.183125054323437, 30.164527714949916, 30.145838489193704, 27.30264579954929, 27.28554229967273, 15.035081932574643, 6.573659764663012, 28.13666803835714, 26.24389570577316, 27.163493488203734, 11.232714428867764, 25.24029326269259, 18.68408948642074, 19.59202423133543, 25.172742632819034, 13.043677186197792, 22.345339580700866, 25.121274335514872, 25.086579431419732, 25.997603152665803, 25.961147927870275, 14.824458093949529, 17.578984649330017, 25.887288941145005, 52.66113335314383, 62.77829476368329, 61.81005199356909, 61.76483115643012, 61.71942217290391, 65.35584459512388, 66.22714780716575, 66.17774442637753, 65.20969307535984, 66.0783330492473, 65.11126528134446, 65.97811652848192, 65.92770672044907, 64.96213641733823, 64.91203082163341, 65.77527295026796, 65.72406076077979, 65.67264836440437, 65.62103591775278, 64.65853991723928, 64.60725023223529, 64.55576374234259, 64.50408060439798, 64.45220097583724, 64.40012501469475, 64.3478528796029, 64.29538472979166, 63.337893672622116, 63.28577847625523, 62.3301352075685, 62.27838462014113, 62.2264443219536, 62.17431447122508, 63.022313998154324, 62.069486747908215, 62.0167891946433, 61.96390272748326, 61.91082750752945, 62.75405012684163, 62.699823216759704, 61.75047095054052, 62.590796578756574, 62.53599718294943, 62.48100729164959, 61.53402954276057, 61.479450168998184, 62.314896322779674, 61.36972975710033, 62.20320628584723, 62.14707695954891, 62.09075832247633, 62.03425054618585, 61.977553802809936, 61.9206682650567, 61.863594106209376, 61.806331500125715, 61.74888062123758, 60.80993819248528, 61.63341474564217, 61.57540010066399, 60.63838077367644, 61.458808279959484, 61.40023145939206, 61.3414676030713, 61.2825168900021, 60.34875979261915, 61.164055612483416, 61.10454540888753, 61.04484907024929, 60.98496677841412, 60.92489871579383, 60.86464506536619, 60.80420601067425, 59.87581628245691, 59.81587567655745, 59.75575286112712, 59.69544801931047, 60.4992361367602, 59.5742929918681, 59.51344317530163, 59.45241207046614, 59.39119986327298, 59.329806740185134, 59.26823288821671, 60.06454340065601, 59.144543748446615, 59.08242883742353, 59.020133951075834, 59.81211810929741, 58.89500501199848, 58.83217134043324, 58.76915845587117, 58.70596655026042, 59.492488509081376, 59.42801813404081, 59.363366730950716, 59.29853449675051, 59.23352162893038, 59.16832832553084, 59.10295478514197, 59.037401206902906, 58.97166779050124, 58.90575473617234, 58.839662244698815, 58.77339051740984, 58.7069397561806, 58.640310163431636, 58.57350194212824, 59.34232265714813, 59.2741982917028, 59.20589336676988, 59.137408090418006, 58.23678854913471, 58.168912849203906, 58.93087224177203, 58.8616676514089, 58.792283758198046, 58.722720773494835, 58.652978909200186, 58.583058377759905, 58.51295939216406, 58.44268216594632, 58.37222691318331, 58.30159384849395, 59.05093506291256, 58.97894718880838, 58.08862993717762, 58.01728778179508, 57.94576889569234, 58.68920129245688, 58.61631732165596, 57.730154034339925, 58.47001393621103, 58.3965949672325, 58.32299811209829, 57.44020660062224, 58.17527164065919, 58.10114247435473, 58.02683632189412, 58.75724720698274, 58.68155082505787, 58.60567568895237, 58.52962202979505, 58.453390079258554, 58.37698006955862, 58.30039223345339, 58.2236268042427, 58.14668401576735, 58.06956410240842, 57.992267299086535, 57.91479384126119, 57.83714396492994, 57.75931790662779, 57.68131590342642, 56.81405410809874, 56.73677425968499, 56.6593215812173, 56.58169630862995, 56.50389867838298, 55.642235470135624, 55.56517913652239, 55.48795354173714, 55.410558921022414, 36.62888435177995, 36.577427980723655, 35.74871422702132, 37.25022753919489, 36.42239096909711, 37.14433006687298, 37.09121152787353, 36.26635541922351, 36.98463565323857, 36.16177908720474, 36.10932560889627, 36.05676213531975, 36.770133269711636, 35.95130584316697, 35.89841334582886, 35.84541149569803, 35.7923004542273, 38.020298280002265, 35.68575144474008, 34.874179465092666, 35.57876761563323, 35.52511305087974, 34.71664069024818, 35.41747943817766, 34.61108580920399, 35.309414274665706, 34.50510920300181, 35.9498745978728, 34.39871216293314, 35.091994567414076, 34.29189598541233, 33.49401958040259, 34.18466197196081, 34.130888684879025, 34.077011429191174, 33.283399274038096, 33.96894566879133, 34.65203483007652, 33.86046600750845, 33.80607137689883, 33.75157376713299, 34.42951624300749, 35.10497767772089, 35.04778927779682, 34.99049411622846, 34.205319609889585, 34.14900953563656, 34.09259543757821, 34.03607748756166, 34.70242300365999, 37.5315318611156, 38.189208919058295, 38.12500941794929, 38.778820079213, 37.27935159782588, 37.21602215259503, 37.86705202053937, 37.08902335601822, 37.025354391532595, 37.67237211526939, 38.316819772972934, 45.333749614370795, 45.25483399594, 33.8818353925774, 44.391955227707406, 49.237629196736314, 49.15071370966242, 49.06364850099061, 48.97643383593663, 49.58748526560248, 49.49872230267514, 45.93024457509373, 51.40471941396691, 51.31173529241127, 51.910738040281636, 51.8161808307655, 51.03184623644067, 51.626593177032674, 51.53156331033286, 50.750558116626955, 51.34103294465278, 50.56225925238025, 50.467878644626005, 50.37334430296104, 50.27865651535334, 50.18381557023834, 50.08882175651801, 49.99367536355997, 50.57267906878039, 49.802925999724344, 49.70732360990239, 49.611569802952246, 49.51566487055663, 50.08744166032963, 49.98993526871007, 50.55750695373257, 50.45839216157151, 50.359123664397195, 50.259701764598695, 50.160126765032345, 50.06039896902086, 49.96051868035243, 49.860486203279706, 49.76030184251898, 49.659965903249166, 49.559478691110954, 50.109614729471694, 50.00749972142531, 49.90523238186225, 49.80281302230656, 49.70024195474536, 47.66514860234373, 49.494645945864704, 48.750171999257155, 51.20877595879766, 51.74019321876464, 51.63134316964509, 50.88625762222233, 52.68263259578947, 52.57061242808793, 66.85163558771795, 65.44932066918469]
plot.plot(json_data["xpoints"], json_data["ypoints"], 'o')
plot.savefig('C:/Users/satan/Projects/TfMiniServer/plots/'+name)
plot.show()

import pymonics as me
import numpy as np

print(me.Memo_esprit().frequency_detection_byCSV(2400,"inputSignalFile.csv"))
inputSignal="1.555037203,1.408682404,1.082233181,0.800207957,0.68369491,0.669075001,0.626269039,0.516688558,0.403207051,0.32593037,0.226662369,0.02752239,-0.23786631,-0.425827785,-0.434851784,-0.330624657,-0.286440107,-0.393009988,-0.565884313,-0.652380118,-0.62091771,-0.599285288,-0.723515083,-0.972306758,-1.185895815,-1.237604966,-1.152048425,-1.045787057,-0.976343471,-0.895748015,-0.755329073,-0.606094362,-0.547208786,-0.579369831,-0.552332151,-0.308300275,0.134551249,0.566568683,0.777677856,0.747239629,0.634025446,0.595036218,0.643717335,0.696930238,0.718325483,0.762929714,0.877111546,0.996786666,0.998136748,0.850380192,0.678593153,0.64102342,0.751509957,0.863869322,0.836777927,0.689177551,0.568594774,0.564496351,0.596027945,0.503058208,0.230365871,-0.114907136,-0.386543255,-0.548064341,-0.671099495,-0.804653648,-0.900537511,-0.893900161,-0.828523561,-0.847721489,-1.031617924,-1.272737982,-1.354205729,-1.164347866,-0.815484645,-0.531944524,-0.43703049,-0.471446189,-0.504199386,-0.490869186,-0.480268721,-0.495166129,-0.464007064,-0.300599853,-0.038953861,0.171294752,0.222427226,0.176573718,0.205229371,0.398144334,0.663360571,0.838150013,0.875439428,0.890530507,1.012805335,1.224348103,1.374892182,1.348988106,1.181906187,0.994380415,0.847182486,0.696014685,0.499051093,0.317750952,0.260822628,0.331893091,0.377461178,0.225225165,-0.120725406,-0.465225308,-0.605191029,-0.521875814,-0.374763192,-0.321919483,-0.380608319,-0.473065077,-0.563345426,-0.700625988,-0.918207163,-1.134403771,-1.211020962,-1.108860508,-0.953186956,-0.904834082,-0.984597441,-1.047760863,-0.952794001,-0.721303776,-0.506081684,-0.407975394,-0.361829281,-0.221467443,0.061221237,0.380810037,0.599559936,0.691846045,0.737310528,0.79029165,0.804585026,0.719910132,0.588091252,0.563871511,0.737821714,1.007301787,1.151495015,1.04768295,0.792561412,0.597315156,0.579248981,0.67422004,0.751833027,0.76456464,0.755343774,0.741852428,0.649646162,0.398528585,0.034799784,-0.274807544,-0.407194566,-0.416445072,-0.472146383,-0.666725594,-0.913071194,-1.048457865,-1.025316379,-0.959553962,-0.986076197,-1.099448312,-1.164766529,-1.081513001,-0.892823539,-0.719186937,-0.613937805,-0.522860995,-0.397747219,-0.294866349,-0.32149408,-0.476661868,-0.59724714,-0.499525104,-0.175397955,0.185977147,0.378394532,0.37302159,0.315533059,0.350443243,0.489059789,0.649435314,0.794580379,0.969712245,1.200913295,1.399770106,1.424383974,1.240661716,0.98549693,0.837103727,0.830613497,0.83064048,0.698090728,0.452608769,0.244314692,0.174891795,0.181150867,0.11700458,-0.071118338,-0.289771007,-0.417011348,-0.442873857,-0.455792554,-0.510644608,-0.555160464,-0.520574998,-0.453282304,-0.504098502,-0.762154162,-1.119962861,-1.347185174,-1.30806567,-1.086215734,-0.886262171,-0.82594707,-0.852115236,-0.846378439,-0.772952284,-0.68236872,-0.595062588,-0.43894137,-0.138769746,0.250525458,0.554349552,0.645018298,0.579965625,0.540322743,0.635601643,0.792356082,0.857591861,0.787245844,0.695751426,0.716970492,0.847469876,0.955906455,0.942833233,0.845893857,0.774909292,0.765486403,0.749123204,0.667166941,0.574513019,0.582954596,0.698627141,0.763147494,0.595539528,0.188169589,-0.264288351,-0.54669478,-0.615495473,-0.602128903,-0.643955738,-0.751851001,-0.853205898,-0.92209814,-1.014986381,-1.164351704,-1.285115039,-1.238086676,-0.995018794,-0.702111945,-0.548047739,-0.572380977,-0.638149199,-0.595150082,-0.446932032,-0.329856042,-0.33580417,-0.398261159,-0.37100507,-0.200322643,0.023562588,0.183562645,0.271849336,0.372754725,0.529662735,0.673927557,0.720838565,0.70602447,0.778422356,1.030704797,1.360511035,1.541535125,1.438449063,1.136233609,0.843364536,0.68834731,0.631845541,0.571418387,0.479722134,0.407644397,0.369116728,0.28035795,0.057414276,-0.251298273,-0.473984302,-0.48659221,-0.352513409,-0.264050652,-0.341328045,-0.517919713,-0.639605837,-0.651084288,-0.653418269,-0.766181257,-0.976180568,-1.14890412,-1.182828783,-1.115290657,-1.050837605,-1.019874888,-0.949557723,-0.784738903,-0.591848593,-0.498699273,-0.527838744,-0.530892027,-0.330966885,0.082400505,0.518948162,0.765372111,0.778045364,0.688372886,0.637727764,0.647243605,0.659126444,0.6635003,0.726641718,0.882834153,1.040884984,1.051941029,0.87920491,0.663997483,0.592111545,0.700245747,0.843359376,0.860019294,0.741319249,0.616153318,0.576639097,0.564690895,0.448991005,0.188135604,-0.117853489,-0.348365664,-0.493493404,-0.635241729,-0.810941027,-0.944761035,-0.947207754,-0.856637662,-0.832273134,-0.982544431,-1.221444687,-1.333916149,-1.188440575,-0.867945018,-0.578952796,-0.448643996,-0.439634443,-0.450066559,-0.449071478,-0.477770625,-0.534019606,-0.518361593,-0.336081813,-0.032203171,0.21594621,0.275847258,0.204488385,0.189382508,0.348593936,0.612547012,0.818732034,0.899771851,0.943173836,1.059508946,1.235008234,1.342600682,1.294571522,1.140230195,0.992658869,0.886261392,0.750479116,0.534043226,0.310349129,0.21594609,0.278733698,0.350009167,0.241658773,-0.071262615,-0.414412454,-0.585952159,-0.546697462,-0.427391398,-0.368081352,-0.39103179,-0.440479402,-0.509005029,-0.659772361,-0.917007247,-1.173957115,-1.265808118,-1.143612455,-0.945104494,-0.85972413,-0.931254674,-1.020903464,-0.969863803,-0.771106991,-0.556181582,-0.426219141,-0.336395988,-0.168585959,0.107367428,0.390578209,0.566487436,0.637349836,0.696546151,0.789750218,0.844716597,0.774574612,0.622079147,0.555337261,0.692172897,0.954138131,1.125089559,1.065033043,0.842416422,0.64776544,0.596959668,0.648267006,0.698939407,0.718617606,0.746035636,0.775560888,0.704036395,0.438716658,0.034970139,-0.315015462,-0.461801349,-0.449924825,-0.463131903,-0.621025469,-0.860102427,-1.022638728,-1.043474337,-1.009632176,-1.036213012,-1.116666354,-1.138551676,-1.028385649,-0.84709661,-0.710605578,-0.647860355,-0.57751336,-0.437565159,-0.294470044,-0.280923166,-0.422313883,-0.564036202,-0.509366629,-0.221691042,0.133025634,0.352941067,0.391707563,0.365853313,0.400239626,0.50563448,0.62257208,0.741212355,0.924322367,1.192684228,1.434147125,1.478975106,1.280264011,0.98433212,0.796208213,0.776133356,0.797943859,0.708385902,0.49901611,0.29694788,0.199765983,0.161819142,0.066162389,-0.120783826,-0.306210299,-0.389869166,-0.389476006,-0.410910953,-0.502975474,-0.590019851,-0.575249898,-0.49231253,-0.502146044,-0.720654301,-1.065624816,-1.315248999,-1.318876716,-1.133128854,-0.93897641,-0.850414411,-0.83244537,-0.795338263,-0.723482686,-0.666516045,-0.623060309,-0.492257635,-0.183277237,0.24347487,0.589579703,0.699679308,0.618596343,0.538092417,0.593889264,0.737904167,0.826308681,0.798726643,0.742645504,0.769495721,0.871258582,0.935774307,0.8916501,0.797042094,0.759662642,0.794206206,0.802905252,0.71130766,0.580468674,0.547145932,0.643860267,0.724864685,0.598324166,0.230284485,-0.21012483,-0.515139941,-0.627434312,-0.649462701,-0.696293556,-0.775189973,-0.832492667,-0.870842359,-0.966296914,-1.149611102,-1.313945991,-1.291836075,-1.038885393,-0.707736707,-0.511648358,-0.517658489,-0.600318284,-0.598572526,-0.489607471,-0.38396137,-0.366777482,-0.385787746,-0.323400747,-0.148397771,0.04635096,0.162458512,0.220419139,0.324455875,0.515481052,0.70315405,0.774794165,0.749533023,0.783648124,0.994029141,1.30555713,1.504066564,1.442471098,1.179045107,0.897432564,0.718731682,0.618951773,0.523503341,0.428023115,0.385556663,0.390983935,0.332167998,0.105751551,-0.237824601,-0.503996315,-0.540436902,-0.395844894,-0.26849284,-0.304373862,-0.463127017,-0.602228863,-0.655677844,-0.696588255,-0.820282634,-1.006010694,-1.13490696,-1.134657333,-1.063824328,-1.029283322,-1.042011005,-1.001491324,-0.832684708,-0.605165853,-0.468695862,-0.473779366,-0.488351353,-0.326863943,0.045131611,0.464163699,0.728775998,0.78308384,0.731894786,0.69149672,0.676694436,0.64510549,0.615017899,0.675323488,0.861779133,1.063638761,1.104165171,0.926876641,0.676544943,0.56144617,0.645930966,0.800812149,0.856385872,0.779406117,0.670894361,0.612766263,0.559149965,0.405162985,0.134517671,-0.146732651,-0.33367594,-0.444647602,-0.583831785,-0.790161572,-0.968009715,-0.999339329,-0.904104217,-0.844349049,-0.951284987,-1.167546548,-1.29161572,-1.18533892,-0.906317961,-0.633741666,-0.484435875,-0.433356452,-0.405637772,-0.395407874,-0.44956444,-0.549295964,-0.567724093,-0.386941582,-0.052372281,0.239654502,0.328190394,0.251658858,0.200865418,0.316932592,0.558123158,0.776877007,0.897581525,0.981801744,1.114310399,1.270484252,1.335824265,1.250273293,1.086842921,0.964821626,0.902069695,0.800051962,0.584898648,0.329927519,0.191814156,0.226257935,0.303313846,0.230818279,-0.039082137,-0.360223753,-0.544560851,-0.545150836,-0.466565104,-0.422864823,-0.425855265,-0.433174969,-0.463994508,-0.606462301,-0.889459432,-1.19027658,-1.31506158,-1.194043149,-0.964141101,-0.834803724,-0.878748779,-0.974455529,-0.959485446,-0.803781969,-0.610778633,-0.467618718,-0.337500972,-0.129130277,0.161809289,0.4249508,0.558355215,0.59191944,0.643460698,0.762938601,0.861585656,0.824235735,0.672799003,0.573900959,0.667017623,0.901329208,1.079042602,1.055257168,0.875480345,0.702061035,0.637706185,0.648879525,0.659143524,0.663911425,0.712264309,0.784000788,0.749632816,0.491989256,0.06125294,-0.332491102,-0.511709763,-0.500095413,-0.481030831,-0.595173987,-0.80711478,-0.976664464,-1.034116395,-1.043305449,-1.090628182,-1.157009672,-1.138540109,-0.988170192,-0.792759247,-0.677045846,-0.656902154,-0.623308681,-0.490610416,-0.32014996,-0.262913412,-0.371947045,-0.514065941,-0.491828929,-0.247785232,0.07991903,0.307478272,0.383098816,0.399793324,0.454683387,0.54574865,0.622170599,0.700585443,0.870028015,1.159691017,1.443883812,1.525219553,1.332843554,1.009616459,0.777705204,0.725595848,0.748365159,0.691528936,0.525851516,0.350165338,0.245041708,0.169895706,0.031831446,-0.175468745,-0.345655342,-0.38851683,-0.348509441,-0.356506718,-0.470322012,-0.600124567,-0.621889948,-0.544918961,-0.527321029,-0.701528445,-1.014863497,-1.265713324,-1.302474632,-1.160317628,-0.99225112,-0.895383823,-0.839819606,-0.760656095,-0.669000417,-0.627466061,-0.624824887,-0.53373474,-0.237762086,0.211686731,0.600195577,0.746442558,0.671154825,0.562436852,0.574169854,0.687116433,0.777001248,0.782731946,0.77059054,0.823104237,0.915908963,0.942869451,0.856372739,0.742130964,0.720835863,0.796269626,0.844790264,0.765681589,0.612505312,0.53565687,0.596600356,0.672618813,0.574659009,0.250595192,-0.158851267,-0.466169321,-0.612154538,-0.677800954,-0.749767064,-0.819557145,-0.838839446,-0.835089176,-0.911498725,-1.111754039,-1.31686775,-1.334016913,-1.093151503,-0.739100957,-0.499709416,-0.470332082,-0.548165146,-0.575432518,-0.510292518,-0.435315824,-0.415380838,-0.40053811,-0.294793919,-0.094524342,0.090261001,0.168336667,0.184264421,0.269597175,0.477440905,0.706815811,0.817188371,0.803769116,0.81446362,0.981418684,1.258014594,1.451834821,1.41974165,1.200239723,0.948892441,0.767051188,0.633249471,0.494184869,0.373948782,0.341955327,0.385762883,0.368829615,0.160280737,-0.200191145,-0.507927751,-0.583396841,-0.449752747,-0.298777337,-0.291126706,-0.415093692,-0.550487621,-0.633457742,-0.718535708,-0.871770135,-1.054233614,-1.148600661,-1.104681457,-1.009782502,-0.985939588,-1.037590071,-1.038550137,-0.887364604,-0.642045633,-0.464197001,-0.430532421,-0.433988216,-0.297133889,0.031442866,0.416061843,0.676900558,0.761465289,0.753856749,0.743253907,0.724322263,0.658097705,0.584913872,0.621253762,0.818769906,1.059455284,1.141340418,0.981483536,0.713243119,0.556184155,0.602623305,0.746994475,0.826971958,0.793437843,0.719381184,0.664133169,0.580321423,0.382331515,0.082518854,-0.194289375,-0.3460141,-0.413912228,-0.529886133,-0.74787121,-0.964680926,-1.037506136,-0.958742687,-0.880583877,-0.945539962,-1.123469179,-1.238146962,-1.156390834,-0.920853563,-0.682367525,-0.535975699,-0.454226657,-0.3825297,-0.343266458,-0.402212335,-0.537304767,-0.598847497,-0.441221314,-0.094640489,0.236767615,0.366700008,0.306033275,0.23642028,0.310668271,0.514049307,0.723041899,0.869126019,0.997132598,1.163168051,1.321597139,1.356042348,1.226362627,1.034430118,0.917705805,0.89058387,0.831610348,0.639315546,0.371894624,0.19398117,0.187703756,0.248448213,0.195490635,-0.032278217,-0.315686325,-0.491019132,-0.516985628,-0.482299503,-0.472174346,-0.476860494,-0.452809614,-0.439630014,-0.553721663,-0.842646878,-1.179430525,-1.347418783,-1.248394509,-1.005519465,-0.836489029,-0.839538284,-0.919784964,-0.924876801,-0.811251788,-0.655918811,-0.520865666,-0.364969682,-0.113006374,0.211537547,0.475546318,0.577678305,0.567406572,0.590720347,0.716358664,0.851158804,0.857057918,0.726968454,0.61498857,0.66810523,0.861909573,1.024379416,1.020961219,0.883364244,0.747413922,0.69084274,0.675657933,0.642058981,0.614182863,0.661806786,0.76560204,0.77481222,0.544412978,0.107367509,-0.322699966,-0.544854106,-0.554692391,-0.521479426,-0.595475031,-0.767294716,-0.92215886,-1.000325788,-1.051794859,-1.136162647,-1.210226378,-1.164704446,-0.970780109,-0.742640998,-0.626814962,-0.6388291,-0.649203206,-0.543361326,-0.366204708,-0.272056474,-0.338376928,-0.45955458,-0.451679261,-0.247893466,0.039505478,0.25299494,0.349622004,0.408865554,0.50071403,0.598779399,0.647733113,0.682567409,0.819588891,1.109770329,1.426317481,1.551542732,1.386241407,1.055409422,0.786243374,0.691565717,0.693962359,0.651850701,0.526547739,0.391159303,0.299382261,0.203153108,0.021994762,-0.221647628,-0.39860765,-0.413892014,-0.329811347,-0.306059219,-0.420818845,-0.583656903,-0.648757207,-0.598372572,-0.57238128,-0.709478934,-0.98064579,-1.211182869,-1.26308464,-1.161495141,-1.033149947,-0.949558971,-0.872367969,-0.750345704,-0.6226445,-0.574748573,-0.599831424,-0.553034153,-0.288325534,0.16198017,0.584107513,0.773940212,0.724593584,0.607410905,0.581548315,0.652244921,0.722050494,0.743804346,0.772149443,0.864204921,0.970209425,0.975028467,0.845539447,0.695444571,0.668364048,0.771996211,0.864377213,0.816462012,0.661922086,0.551720835,0.568654677,0.618872929,0.529976326,0.243746487,-0.123720225,-0.411694818,-0.573422733,-0.680227873,-0.791385831,-0.873869151,-0.870320762,-0.823822396,-0.864540377,-1.059233402,-1.293140456,-1.354042413,-1.144106898,-0.788208885,-0.51501184,-0.44200545,-0.494451818,-0.531081703,-0.503737096,-0.471183329,-0.470019504,-0.438862538,-0.291885027,-0.052537048,0.144607973,0.199407477,0.172307426,0.222187761,0.425358573,0.683541504,0.837873113,0.855060085,0.863236483,0.996059844,1.229071976,1.398209888,1.37568587,1.194516886,0.985038689,0.821701851,0.670980705,0.490854707,0.331353051,0.287907605,0.355101842,0.381383071,0.208097395,-0.148292435,-0.485289771,-0.60459654,-0.501204184,-0.347526599,-0.305417728,-0.385767383,-0.496697164,-0.589872972,-0.713177315,-0.908289493,-1.108956823,-1.185994516,-1.10089895,-0.966965619,-0.931911835,-1.007188817,-1.051594759,-0.935335591,-0.693945821,-0.486236295,-0.408820203,-0.382585529,-0.248930254,0.04517091,0.386193631,0.623158285,0.718048305,0.749599165,0.780457762,0.779072832,0.695131606,0.580351209,0.578136963,0.764868884,1.029968352,1.154984145,1.029732376,0.764858295,0.577797124,0.580145722,0.695089998,0.779317393,0.780401586,0.749790896,0.718265459,0.623172273,0.386282203,0.044938467,-0.248948548,-0.382648273,-0.408905694,-0.486242226,-0.693895047,-0.935336864,-1.051599582,-1.007172713,-0.932004343,-0.966842326,-1.100708996,-1.186071588,-1.109023678,-0.908450154,-0.713097724,-0.590111073,-0.496607716,-0.385880739,-0.305330312,-0.347419272,-0.50115491,-0.604569572,-0.485102817,-0.1482135,0.207936677,0.381167949,0.354954533,0.287840198,0.33136068,0.49086482,0.670891908,0.821754202,0.985290212,1.194545461,1.375751482,1.398297641,1.22910351,0.996133213,0.863207721,0.854914356,0.837907311,0.683390405,0.425505512,0.222555518,0.17225859,0.199383503,0.144619199,-0.052523287,-0.291850121,-0.438714514,-0.469987879,-0.471137198,-0.503989451,-0.530974326,-0.494553497,-0.442129011,-0.515199296,-0.78829455,-1.144180494,-1.354087304,-1.292988188,-1.059208716,-0.864715742,-0.823674151,-0.870561648,-0.873851313,-0.791639416,-0.680127392,-0.573200066,-0.411705617,-0.123640671,0.24347964,0.529830841,0.6188899,0.568917051,0.551651178,0.661944622,0.816304307,0.864160604,0.771929249,0.668256676,0.695377388,0.845609454,0.974840693,0.970338978,0.864419999,0.772079213,0.743764497,0.722142297,0.652226471,0.581574868,0.60740149,0.724584128,0.773836032,0.583874829,0.162116734,-0.288366199,-0.552696618,-0.5998469,-0.574738252,-0.622575227,-0.750364267,-0.87240132,-0.94983568,-1.033357635,-1.161471682,-1.263096571,-1.211014088,-0.980289835,-0.709636548,-0.572467533,-0.598159985,-0.648641904,-0.583340881,-0.420715984,-0.306011787,-0.329685751,-0.413746127,-0.39849383,-0.221685312,0.022096329,0.202915998,0.299356501,0.390718818,0.526367386,0.651740256,0.69375093,0.691857757,0.785978399,1.055146378,1.386166325,1.551591048,1.426345206,1.109658797,0.819459628,0.682553732,0.647977437,0.598738193,0.500531385,0.409004709,0.349714038,0.252936397,0.039564462,-0.247958139,-0.451605037,-0.459441691,-0.33844258,-0.271851101,-0.366227777,-0.543536169,-0.649314862,-0.638954466,-0.627081544,-0.742548794,-0.970749325,-1.164826143,-1.210179607,-1.136313202,-1.051845215,-1.000053051,-0.922080909,-0.767135709,-0.595617372,-0.52143462,-0.554710354,-0.544963202,-0.322704842,0.107335204,0.544676073,0.774864286,0.765622702,0.661936859,0.614081858,0.642158934,0.675720688,0.691003143,0.747376856,0.88345208,1.021036441,1.024323385,0.861814237,0.668434391,0.61510863,0.727139562,0.85700398,0.851352101,0.716156483,0.590685978,0.567259977,0.577618683,0.475790831,0.211660211,-0.112832183,-0.364946908,-0.520879136,-0.655718394,-0.811252854,-0.924763736,-0.919665829,-0.839560195,-0.836822222,-1.005805601,-1.248433287,-1.347323319,-1.179536353,-0.842799084,-0.55371028,-0.439772229,-0.452748481,-0.47694398,-0.472292559,-0.482442928,-0.517113564,-0.491060103,-0.315498052,-0.032120507,0.195575429,0.248347052,0.187592268,0.194115044,0.371935029,0.639254238,0.831449449,0.890614951,0.917768939,1.034483669,1.226246695,1.355851248,1.321624477,1.163245588,0.997162287,0.869222207,0.723013682,0.513999347,0.310782749,0.236447854,0.30614689,0.366594823,0.236672656,-0.094653803,-0.441072196,-0.598829608,-0.537324809,-0.402130062,-0.343388055,-0.382507316,-0.454156235,-0.535748316,-0.682503169,-0.92086646,-1.156802876,-1.238054144,-1.123604498,-0.945579779,-0.880460408,-0.958592296,-1.037427944,-0.96471085,-0.747678111,-0.529767937,-0.414019595,-0.34626634,-0.194275761,0.0825053,0.382449903,0.58023358,0.664191944,0.719376495,0.793368072,0.827022445,0.746983221,0.602303966,0.556293272,0.713096536,0.981446533,1.141399589,1.059665778,0.818790819,0.621255257,0.584881928,0.658187221,0.724446983,0.74337278,0.754109418,0.761602698,0.677010506,0.415987488,0.031358739,-0.297252597,-0.434407022,-0.430606329,-0.463867502,-0.642017742,-0.887511147,-1.038390242,-1.037614131,-0.985829248,-1.009784328,-1.104859672,-1.148474235,-1.054278636,-0.8718638,-0.718281561,-0.633443797,-0.550530111,-0.415421517,-0.291283068,-0.298827384,-0.44960383,-0.583287934,-0.507811096,-0.200330022,0.160425325,0.368932303,0.385659118,0.34192365,0.373966865,0.494262405,0.633082409,0.76704545,0.948942709,1.200101237,1.4195683,1.451821004,1.258017946,0.981414289,0.814486789,0.803733303,0.817097732,0.706845813,0.477563241,0.269734471,0.184454374,0.168155213,0.090267684,-0.094471053,-0.294777364,-0.40030598,-0.415403883,-0.435195223,-0.510234469,-0.575094455,-0.54804764,-0.4703722,-0.499579916,-0.739143301,-1.093023972,-1.333974082,-1.316867648,-1.111276067,-0.911761244,-0.835260336,-0.838778538,-0.819785538,-0.749728005,-0.677674443,-0.612225949,-0.466357268,-0.159065762,0.250647241,0.574513337,0.672564641,0.596676501,0.535909309,0.612472887,0.765491729,0.844611362,0.796289812,0.720685186,0.742371319,0.856475994,0.942790721,0.915828191,0.82300716,0.770744511,0.782903748,0.776859302,0.687254696,0.574299288,0.562454832,0.671068842,0.746442957,0.600424503,0.211514767,-0.237731939,-0.533903108,-0.624685743,-0.627556511,-0.66913438,-0.76066904,-0.839845165,-0.895225299,-0.992271764,-1.160382173,-1.302403988,-1.265638628,-1.014804264,-0.70130462,-0.527229878,-0.544918128,-0.621834176,-0.600182315,-0.470464092,-0.356472582,-0.348314396,-0.388602702,-0.345711342,-0.175629907,0.031653245,0.169840983,0.245038225,0.350327376,0.526004084,0.691729144,0.748360547,0.725747784,0.777598527,1.00971357,1.332965019,1.525289826,1.443683889,1.159977026,0.869881711,0.700470982,0.621961889,0.545753259,0.454913329,0.399690589,0.383215476,0.30739275,0.079924887,-0.248020671,-0.491975805,-0.513821128,-0.371911833,-0.262754965,-0.320132398,-0.490490043,-0.623245343,-0.656892178,-0.677073729,-0.792802439,-0.98832998,-1.13837933,-1.157092158,-1.090712544,-1.043210989,-1.034389791,-0.976675128,-0.807177966,-0.595062746,-0.480875609,-0.500341095,-0.51181992,-0.332453985,0.061287241,0.491648427,0.749488922,0.784038936,0.712261113,0.663992719,0.65901365,0.648716899,0.637640155,0.702082693,0.875539914,1.055407749,1.079026967,0.901465751,0.667047328,0.573892156,0.672634939,0.824510466,0.86175077,0.762784722,0.643214952,0.591983218,0.558493955,0.424774601,0.162163589,-0.129096685,-0.337537012,-0.467495948,-0.610767785,-0.803707406,-0.959606667,-0.974503694,-0.878611127,-0.834759411,-0.964315285,-1.193936816,-1.315300262,-1.190394488,-0.889526171,-0.606142425,-0.464083448,-0.43315738,-0.42593631,-0.423095256,-0.466475973,-0.545039999,-0.544601018,-0.360010514,-0.039111765,0.230842449,0.303165521,0.226250042,0.191578042,0.330106995,0.584964474,0.799892609,0.902195232,0.964917826,1.08675346,1.249997161,1.335932502,1.270493281,1.114305187,0.981807325,0.8975117,0.776764753,0.558235584,0.317147137,0.200882687,0.251494258,0.328356939,0.239581856,-0.052501168,-0.38701143,-0.567549746,-0.549361825,-0.449606889,-0.395361837,-0.405799225,-0.433425446,-0.48442959,-0.633695977,-0.906252152,-1.185392233,-1.29178085,-1.167532495,-0.951359976,-0.844225013,-0.90402043,-0.99967098,-0.967999739,-0.790348702,-0.583803605,-0.444717522,-0.33352981,-0.146482132,0.134378585,0.405119423,0.559131551,0.6127593,0.670750964,0.779314986,0.856341925,0.800883182,0.646006019,0.561410479,0.67650927,0.926934631,1.103891752,1.063539742,0.861470885,0.675287405,0.615257391,0.645012909,0.676667367,0.691473683,0.731830138,0.783188659,0.728710184,0.464389862,0.044941693,-0.3269684,-0.488195983,-0.473696693,-0.468589946,-0.605033728,-0.832854891,-1.00143006,-1.042191012,-1.029102093,-1.063731559,-1.134494702,-1.134827574,-1.006039125,-0.820256365,-0.696514439,-0.655694429,-0.60231657,-0.46314096,-0.304329348,-0.268513615,-0.395719278,-0.540324226,-0.503945431,-0.237669499,0.105601037,0.331862796,0.390848023,0.385627196,0.42772194,0.523385044,0.618952078,0.718757563,0.897542635,1.179044197,1.442448503,1.503992781,1.305647355,0.993971944,0.78361835,0.749658962,0.774754159,0.703223752,0.515476451,0.324290465,0.220401,0.162252267,0.046312144,-0.148222498,-0.323462912,-0.385577179,-0.366616713,-0.38405191,-0.489692225,-0.598299114,-0.600346064,-0.517578815,-0.511644319,-0.707929339,-1.038931023,-1.292088174,-1.314104397,-1.149801406,-0.966358281,-0.870785636,-0.832525649,-0.775357043,-0.696296259,-0.649384789,-0.627349446,-0.51532658,-0.210049124,0.230401276,0.598460551,0.724883706,0.643850321,0.547070312,0.58074609,0.711421648,0.80289696,0.794033164,0.759633556,0.797276586,0.891570638,0.935846986,0.871302859,0.769313623,0.742688551,0.798623964,0.826026515,0.738032512,0.593761655,0.538078624,0.618454762,0.699599508,0.589502463,0.243766661,-0.183308928,-0.492360794,-0.623098097,-0.666806702,-0.72367208,-0.795343893,-0.832168212,-0.850549595,-0.938811532,-1.133072339,-1.318881966,-1.315127699,-1.065338368,-0.720781008,-0.502337576,-0.492222376,-0.575502163,-0.589998165,-0.502898788,-0.410871609,-0.389449729,-0.389891945,-0.306123789,-0.120705756,0.066099526,0.161767444,0.199648306,0.297000859,0.499203324,0.708589435,0.79811818,0.776062038,0.796143755,0.984374785,1.280063873,1.47901487,1.43417845,1.192952185,0.924533312,0.741066642,0.622758768,0.505809269,0.400087064,0.365740184,0.391684646,0.353077169,0.132940325,-0.221743117,-0.50938171,-0.564211192,-0.421993534,-0.280943032,-0.294304516,-0.437451436,-0.577560969,-0.647909279,-0.710814725,-0.847086254,-1.028492929,-1.138349563,-1.11683036,-1.036444362,-1.009824693,-1.043171528,-1.022503471,-0.859875812,-0.620929417,-0.463065097,-0.449727642,-0.461720996,-0.315126572,0.034899308,0.438574065,0.703977495,0.775306321,0.746100389,0.718548931,0.698775168,0.64815193,0.597071489,0.64794122,0.842424061,1.065144939,1.125132411,0.954055776,0.692214602,0.555430848,0.622186826,0.774537022,0.844785827,0.789895906,0.696763938,0.637240026,0.566503107,0.390637241,0.107436527,-0.16858006,-0.336266448,-0.426356906,-0.556586506,-0.771279599,-0.969946717,-1.020842436,-0.931335812,-0.859594075,-0.945110825,-1.14345365,-1.265634354,-1.17382135,-0.916834124,-0.659628855,-0.508973656,-0.440601778,-0.391016396,-0.368236217,-0.42739861,-0.546545898,-0.585916795,-0.414678798,-0.071204113,0.241671898,0.349821073,0.278745297,0.216011029,0.310426817,0.534108084,0.75062992,0.886261133,0.992872084,1.140469154,1.294769501,1.342731571,1.235242617,1.0595842,0.943080947,0.899817443,0.818664831,0.612526758,0.348752202,0.189381395,0.20446112,0.275708514,0.215967239,-0.032188083,-0.336027382,-0.518811978,-0.533875496,-0.477799237,-0.44898086,-0.449958076,-0.439674792,-0.448620898,-0.578971938,-0.868145092,-1.188223408,-1.334025903,-1.221661026,-0.98259797,-0.832316361,-0.856729689,-0.947367672,-0.944926758,-0.810807308,-0.635269099,-0.493354608,-0.348117452,-0.117875982,0.188143601,0.448978987,0.564845983,0.576437067,0.616048746,0.741454506,0.85990669,0.843428048,0.700255295,0.592248582,0.663923692,0.879242132,1.051943785,1.040679329,0.882902519,0.726824351,0.663417234,0.659233121,0.64714984,0.637715759,0.688219565,0.777918508,0.765489804,0.519077419,0.082617408,-0.330901623,-0.531040479,-0.527735589,-0.49902781,-0.591941462,-0.784742079,-0.949559111,-1.019934405,-1.050932989,-1.115197451,-1.182853794,-1.148595655,-0.976189261,-0.766342346,-0.653358614,-0.651126797,-0.639591092,-0.517645377,-0.341151006,-0.26391935,-0.35235675,-0.486523871,-0.474218562,-0.251468337,0.057403904,0.280695626,0.369037412,0.407941244,0.479502689,0.571474767,0.631950516,0.688138928,0.843680226,1.136034952,1.438319248,1.541348641,1.360336603,1.030562794,0.778503738,0.706218456,0.720987139,0.674146794,0.529625853,0.373006712,0.271848764,0.183652833,0.023603076,-0.200481839,-0.371412705,-0.398253167,-0.335947008,-0.32978795,-0.447015968,-0.594983326,-0.638296001,-0.572322521,-0.54783035,-0.702132454,-0.995072419,-1.238087028,-1.285185739,-1.164529787,-1.015071227,-0.922187082,-0.85327468,-0.75209744,-0.644091614,-0.60214573,-0.615435318,-0.546484706,-0.264348108,0.188412827,0.5953894,0.763330743,0.69854822,0.582709927,0.574524378,0.666844672,0.749339579,0.765876002,0.774817543,0.84599821,0.942787623,0.955970635,0.847615633,0.717052783,0.695665306,0.787116404,0.857763307,0.792288309,0.635482696,0.540408792,0.579705687,0.644843675,0.554134702,0.250473636,-0.138624994,-0.438872423,-0.595052636,-0.682304802,-0.772983207,-0.846412306,-0.851886744,-0.82607543,-0.886179436,-1.086363058,-1.307914442,-1.347249988,-1.119835581,-0.762153258,-0.504177838,-0.453194089,-0.520665567,-0.555313538,-0.510458786,-0.455846322,-0.442772605,-0.417004586,-0.289982134,-0.07137728,0.116854185,0.180748426,0.174610307,0.244125567,0.452681652,0.698443126,0.830683138,0.830513299,0.837195346,0.985548142,1.240735252,1.424638651,1.39976748,1.200695188,0.969860611,0.79441941,0.649437039,0.489058066,0.350489936,0.315370877,0.37320002,0.378259717,0.185680872,-0.175580878,-0.499582676,-0.59718873,-0.476794192,-0.321489781,-0.294972382,-0.397765313,-0.522901657,-0.613728491,-0.719170036,-0.892798561,-1.081648836,-1.164856661,-1.099316292,-0.98611889,-0.959339919,-1.025319735,-1.048441211,-0.913073442,-0.6667331,-0.472049846,-0.416349841,-0.407381961,-0.274792998,0.03505852,0.398391373,0.649590161,0.741955118,0.755259317,0.764524154,0.751936788,0.673915543,0.578958513,0.59743183,0.792566218,1.047656285,1.151674913,1.007286279,0.737945621,0.563873274,0.588010396,0.720007669,0.804820471,0.790184551,0.737271426,0.691664525,0.599603731,0.380750428,0.061293994,-0.221604079,-0.361761417,-0.407971548,-0.506077779,-0.721481365,-0.953030924,-1.047876056,-0.984663655,-0.905187207,-0.953265788,-1.109334251,-1.210953562,-1.134558432,-0.918063202,-0.700726844,-0.563251904,-0.473146821,-0.38058017,-0.321781384,-0.374749768,-0.521909648,-0.605183083,-0.46539945,-0.120946537,0.225474275,0.377118053,0.332210722,0.26095882,0.317920803,0.499196936,0.695979303,0.847278535,0.994435699,1.181765156,1.349205865,1.37494527,1.224226741,1.012794962,0.890713372,0.875306542,0.838203993,0.663561345,0.397956456,0.205224729,0.176684871,0.222620896,0.171325996,-0.039202521,-0.300606661,-0.463969303,-0.495353028,-0.480340141,-0.490963509,-0.504241745,-0.471361855,-0.437496133,-0.531875601,-0.815577867,-1.164374612,-1.354112622,-1.27285252,-1.031715583,-0.847738521,-0.828307882,-0.893593586,-0.900599122,-0.804660956,-0.67108316,-0.548304752,-0.386627072,-0.114938623,0.230445911,0.50311778,0.595880251,0.564478338,0.568821783,0.689220641,0.836594474,0.864122717,0.751552148,0.640830115,0.678638158,0.850251193,0.99825436,0.996972981,0.8770349,0.762857686,0.718262686,0.697109079,0.64376595,0.595042926,0.634317303,0.747228995,0.777758871,0.566498724,0.134386834,-0.307937215,-0.55236341,-0.579076503,-0.547433476,-0.605999031,-0.7555061,-0.895833788,-0.976228143,-1.045777333,-1.151909152,-1.237557887,-1.186003214,-0.972270009,-0.72329087,-0.599290309,-0.620841241,-0.652509689,-0.565976256,-0.393202648,-0.286281301,-0.330867519,-0.434769809,-0.425719713,-0.237862129,0.027540964,0.226456061,0.325900981,0.40308813,0.516744385,0.626183186,0.669014172,0.683727747,0.800362539,1.081994216,1.408627045,1.555067157,1.408596371,1.082342266,0.800121182,0.683762041,0.669127364,0.626016623,0.516767014,0.402999627,0.325883949,0.226701785,0.027610543,-0.237815611,-0.425855194,-0.434911781,-0.330863505,-0.286502398,-0.393082111,-0.566003381,-0.65236454,-0.621052021,-0.599306388,-0.72334582,-0.972183442,-1.186097191,-1.237381784,-1.151894201,-1.045916878,-0.976315703,-0.895721168,-0.75548458,-0.605993764,-0.547507331,-0.579172407,-0.552231237,-0.308178347,0.134539123,0.566559181,0.778020207,0.747264985,0.634080335,0.595027059,0.643627494,0.697003793,0.718330206,0.762866126,0.877193314,0.997006724,0.998097558,0.850472707,0.678791867,0.640863033,0.751499426,0.864027284,0.836522222,0.689362927,0.568746959,0.564591133,0.595961269,0.503055263,0.230538385,-0.114993252,-0.386489402,-0.548079055,-0.670913508,-0.804653904,-0.90063842,-0.893734704,-0.828318022,-0.847633847,-1.031773067,-1.272654866,-1.354180514,-1.16422689,-0.81559944,-0.531952258,-0.437354474,-0.471387531,-0.504242967,-0.490600198,-0.480290534,-0.495455339,-0.463969112,-0.300576426,-0.039183508,0.17128672,0.222251082,0.176703749,0.205231342,0.397988302,0.66328367,0.838112625,0.875501406,0.890495164,1.012904151,1.224222679,1.374804496,1.349110901,1.181651425,0.994564348,0.847064145,0.69593341,0.499422753,0.31776693,0.260905341,0.332187301,0.377283491,0.225591057,-0.120669438,-0.465277727,-0.60502518,-0.521729637,-0.374808592,-0.322048003,-0.380758835,-0.473314669,-0.563277215,-0.700698263,-0.917980402,-1.134562429,-1.210892784,-1.109137578,-0.952939949,-0.905017266,-0.984480137,-1.04794814,-0.952852608,-0.721473498,-0.506147964,-0.407757672,-0.361696719,-0.221590718,0.061257626,0.380806094,0.599415523,0.69153128,0.737154783,0.790213772,0.80488378,0.719966393,0.588211342,0.563889972,0.737929178,1.007425414,1.151469627,1.047490433,0.792472166,0.597404237,0.578852266,0.674116377,0.751883471,0.764476952,0.755356368,0.741946523,0.649545717,0.398498877,0.034881835,-0.274742553,-0.407169215,-0.416326957,-0.471839191,-0.666752683,-0.912999927,-1.048239325,-1.025274802,-0.959533259,-0.9862505,-1.099159319,-1.164578599,-1.081511717,-0.892796514,-0.71934069,-0.613862635,-0.522924952,-0.397763629,-0.295102083,-0.321688193,-0.476575748,-0.597303152,-0.49960907,-0.175370904,0.185703822,0.378299074,0.37314154,0.315300285,0.350557081,0.488953002,0.649422384,0.794569628,0.969726757,1.200639407,1.399840597,1.424285077,1.240452785,0.98547418,0.837290667,0.830680843,0.830707613,0.698350229,0.452579709,0.244275724,0.174984767,0.180997453,0.11697746,-0.071255734,-0.289857522,-0.417047121,-0.442830171,-0.455891967,-0.510449387,-0.555168189,-0.520720116,-0.453164663,-0.504161002,-0.761891496,-1.120041553,-1.347429449,-1.307967271,-1.086366437,-0.886365802,-0.826104454,-0.851799803,-0.846264362,-0.772885392,-0.682589513,-0.59535563,-0.438855536,-0.138897298,0.250744007,0.554312061,0.645138307,0.579675823,0.540453151,0.635609553,0.792431876,0.85772146,0.787079391,0.695505663,0.717037646,0.847501213,0.955986815,0.94274573,0.846159771,0.774750517,0.76558411,0.749480821,0.66731391,0.574380401,0.582735186,0.698580016,0.76307031,0.595517808,0.188247092,-0.264257058,-0.546715588,-0.615382689,-0.602122922,-0.644118594,-0.752025476,-0.853348249,-0.921852343,-1.015035689,-1.164481929,-1.285196093,-1.238104818,-0.99485378,-0.702310327,-0.547956171,-0.572283847,-0.638196515,-0.595146593,-0.446854365,-0.329883275,-0.33576776,-0.398212128,-0.37099319,-0.200279414,0.023613652,0.183596119,0.271824613,0.372937765,0.529720503,0.673907814,0.720872642,0.706044613,0.77829417,1.030426382,1.360520278,1.541339314,1.43827684,1.136119574,0.843555096,0.688377009,0.631732743,0.571339281,0.479448801,0.407693368,0.368947615,0.280571433,0.057456458,-0.251336823,-0.473998674,-0.486365204,-0.352523974,-0.264091336,-0.341427132,-0.518063572,-0.639446921,-0.651279265,-0.653389483,-0.766288084,-0.976163411,-1.148699638,-1.182764672,-1.115349728,-1.051106101,-1.020039061,-0.949843141,-0.784828204,-0.591932409,-0.498844492,-0.527847067,-0.531144503,-0.331215418,0.082658646,0.518950475,0.765397826,0.777871248,0.68828254,0.637741031,0.64708626,0.659278771,0.663451199,0.726782331,0.882942557,1.040837113,1.052086367,0.879066982,0.664150973,0.592322201,0.700217119,0.843443142,0.859856686,0.741489247,0.615944256,0.576410791,0.564667913,0.448882087,0.188496417,-0.117587329,-0.348282901,-0.493355751,-0.635443865,-0.810987608,-0.94484857,-0.947279985,-0.856553528,-0.832288964,-0.982621908,-1.221556172,-1.334010275,-1.18822588,-0.867771169,-0.579136538,-0.448766329,-0.439814106,-0.450174233,-0.448975235,-0.477851293,-0.534211349,-0.5186669,-0.335822811,-0.03222406,0.215838832,0.275747802,0.204386778,0.189295177,0.348831152,0.612470702,0.818650337,0.899981309,0.943244809,1.05968326,1.234971441,1.342956994,1.294582832,1.140255825,0.992747199,0.886380265,0.750670814,0.534013605,0.310327154,0.215875284,0.278727258,0.349863196,0.241645211,-0.07134283,-0.414520667,-0.58603467,-0.546769066,-0.427527689,-0.368140378,-0.390973589,-0.440458108,-0.508961651,-0.659717647,-0.916800184,-1.173888548,-1.26567228,-1.143315013,-0.945122424,-0.859790823,-0.93133826,-1.020962712,-0.969817469,-0.771303071,-0.556375958,-0.426662509,-0.336391758,-0.168839785,0.107475203,0.390442129,0.566559794,0.637203244,0.696573372,0.789715028,0.844663302,0.774489096,0.622126523,0.555461341,0.692278044,0.954200204,1.125126955,1.065050349,0.842320673,0.647732225,0.597093038,0.648322373,0.698856096,0.71855417,0.74621415,0.775642425,0.704040576,0.438542549,0.034905205,-0.315020629,-0.461960703,-0.45003544,-0.462941535,-0.620917131,-0.86000965,-1.022545076,-1.043227806,-1.009805276,-1.036161447,-1.116814119,-1.138386604,-1.028394568,-0.847221849,-0.710854581,-0.647750481,-0.577378637,-0.437406719,-0.294311337,-0.280779432,-0.422244888,-0.564146149,-0.509300963,-0.221623317,0.13284332,0.353116512,0.391870406,0.365826899,0.400246317,0.505886633,0.622578571,0.74125501,0.924463236,1.192705248,1.434246807,1.479117483,1.280127422,0.984309408,0.796274754,0.776193782,0.798170859,0.708518254,0.499009634,0.29694612,0.19975011,0.161810824,0.066222193,-0.120883016,-0.30628819,-0.389583324,-0.389333649,-0.41086355,-0.502929867,-0.590033738,-0.575257272,-0.492223623,-0.502327503,-0.720663897,-1.06553393,-1.315188973,-1.318768742,-1.133117997,-0.938845399,-0.850474768,-0.832279438,-0.795256482,-0.72378831,-0.666517951,-0.623174462,-0.492339994,-0.183152535,0.243709177,0.589478656,0.699843326,0.618435118,0.538041548,0.593815704,0.738074513,0.826055086,0.798616732,0.742713923,0.769450032,0.871372419"

print(me.Memo_esprit().frequency_detection_byString(2400,inputSignal))
inputSignalSplit=np.array(inputSignal.split(','))
print(inputSignalSplit.shape)
print(me.Memo_esprit().frequency_detection_byNParray(2400,inputSignalSplit,autocorrelationMatrixSize=44)) ###+++make sure autocoorelationmatrix size is even number

print(me.Passive_filters().single_tuned_filter(7,2.0,0.8,50.0,11))
print(me.Passive_filters().high_pass_filter(7,2.0,0.8,50.0,11))
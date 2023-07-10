# this package
from chemistry_tools.spectrum_similarity import SpectrumSimilarity, create_array, spectrum_similarity


def test_spectrum_similarity():
	diphenylamine = create_array(
			mz=[
					27,
					28,
					32,
					37,
					38,
					39,
					40,
					41,
					50,
					51,
					52,
					53,
					57,
					59,
					61,
					62,
					63,
					64,
					65,
					66,
					67,
					70,
					71,
					72,
					73,
					74,
					75,
					76,
					77,
					78,
					84,
					87,
					88,
					89,
					90,
					91,
					92,
					93,
					101,
					102,
					103,
					104,
					113,
					114,
					115,
					116,
					117,
					126,
					127,
					128,
					129,
					130,
					139,
					140,
					141,
					142,
					143,
					152,
					153,
					154,
					166,
					167,
					168,
					169,
					170,
					171
					],
			intensities=[
					138,
					210,
					59,
					70,
					273,
					895,
					141,
					82,
					710,
					2151,
					434,
					49,
					41,
					121,
					73,
					229,
					703,
					490,
					1106,
					932,
					68,
					159,
					266,
					297,
					44,
					263,
					233,
					330,
					1636,
					294,
					1732,
					70,
					86,
					311,
					155,
					219,
					160,
					107,
					65,
					111,
					99,
					188,
					107,
					120,
					686,
					150,
					91,
					46,
					137,
					201,
					73,
					69,
					447,
					364,
					584,
					279,
					182,
					37,
					60,
					286,
					718,
					3770,
					6825,
					9999,
					1210,
					85
					]
			)

	ethyl_centralite = create_array(
			mz=[
					15,
					26,
					27,
					29,
					30,
					37,
					38,
					39,
					40,
					41,
					42,
					43,
					44,
					50,
					51,
					52,
					53,
					54,
					56,
					62,
					63,
					64,
					65,
					66,
					67,
					68,
					70,
					73,
					74,
					75,
					76,
					77,
					78,
					79,
					80,
					88,
					89,
					90,
					91,
					92,
					93,
					94,
					95,
					102,
					103,
					104,
					105,
					106,
					107,
					115,
					116,
					117,
					118,
					119,
					120,
					121,
					122,
					123,
					127,
					128,
					130,
					131,
					132,
					133,
					134,
					135,
					136,
					139,
					140,
					141,
					146,
					148,
					149,
					150,
					151,
					152,
					153,
					154,
					163,
					164,
					165,
					166,
					167,
					168,
					169,
					175,
					176,
					177,
					179,
					180,
					181,
					182,
					183,
					193,
					194,
					195,
					196,
					197,
					198,
					209,
					210,
					211,
					212,
					223,
					237,
					238,
					239,
					240,
					241,
					251,
					253,
					254,
					267,
					268,
					269,
					270
					],
			intensities=[
					10,
					10,
					240,
					980,
					30,
					10,
					30,
					180,
					30,
					50,
					90,
					10,
					90,
					100,
					700,
					110,
					30,
					20,
					10,
					20,
					140,
					210,
					400,
					110,
					20,
					10,
					10,
					20,
					20,
					30,
					90,
					3830,
					410,
					160,
					30,
					10,
					20,
					70,
					470,
					1140,
					700,
					90,
					10,
					20,
					200,
					1120,
					650,
					480,
					40,
					10,
					10,
					50,
					340,
					410,
					9999,
					1300,
					100,
					10,
					10,
					10,
					10,
					10,
					30,
					10,
					60,
					20,
					10,
					10,
					10,
					10,
					20,
					7889,
					940,
					70,
					10,
					20,
					10,
					10,
					180,
					1010,
					110,
					30,
					60,
					40,
					10,
					110,
					20,
					10,
					10,
					30,
					30,
					190,
					30,
					10,
					10,
					30,
					130,
					60,
					10,
					10,
					20,
					40,
					10,
					20,
					10,
					10,
					170,
					30,
					10,
					10,
					70,
					10,
					290,
					2940,
					590,
					60
					]
			)

	assert spectrum_similarity(diphenylamine, diphenylamine, print_graphic=False)[0] > 0.99
	assert spectrum_similarity(diphenylamine, ethyl_centralite, print_graphic=False)[0] < 0.99


def test_SpectrumSimilarity_class():
	diphenylamine = create_array(
			mz=[
					27,
					28,
					32,
					37,
					38,
					39,
					40,
					41,
					50,
					51,
					52,
					53,
					57,
					59,
					61,
					62,
					63,
					64,
					65,
					66,
					67,
					70,
					71,
					72,
					73,
					74,
					75,
					76,
					77,
					78,
					84,
					87,
					88,
					89,
					90,
					91,
					92,
					93,
					101,
					102,
					103,
					104,
					113,
					114,
					115,
					116,
					117,
					126,
					127,
					128,
					129,
					130,
					139,
					140,
					141,
					142,
					143,
					152,
					153,
					154,
					166,
					167,
					168,
					169,
					170,
					171
					],
			intensities=[
					138,
					210,
					59,
					70,
					273,
					895,
					141,
					82,
					710,
					2151,
					434,
					49,
					41,
					121,
					73,
					229,
					703,
					490,
					1106,
					932,
					68,
					159,
					266,
					297,
					44,
					263,
					233,
					330,
					1636,
					294,
					1732,
					70,
					86,
					311,
					155,
					219,
					160,
					107,
					65,
					111,
					99,
					188,
					107,
					120,
					686,
					150,
					91,
					46,
					137,
					201,
					73,
					69,
					447,
					364,
					584,
					279,
					182,
					37,
					60,
					286,
					718,
					3770,
					6825,
					9999,
					1210,
					85
					]
			)

	ethyl_centralite = create_array(
			mz=[
					15,
					26,
					27,
					29,
					30,
					37,
					38,
					39,
					40,
					41,
					42,
					43,
					44,
					50,
					51,
					52,
					53,
					54,
					56,
					62,
					63,
					64,
					65,
					66,
					67,
					68,
					70,
					73,
					74,
					75,
					76,
					77,
					78,
					79,
					80,
					88,
					89,
					90,
					91,
					92,
					93,
					94,
					95,
					102,
					103,
					104,
					105,
					106,
					107,
					115,
					116,
					117,
					118,
					119,
					120,
					121,
					122,
					123,
					127,
					128,
					130,
					131,
					132,
					133,
					134,
					135,
					136,
					139,
					140,
					141,
					146,
					148,
					149,
					150,
					151,
					152,
					153,
					154,
					163,
					164,
					165,
					166,
					167,
					168,
					169,
					175,
					176,
					177,
					179,
					180,
					181,
					182,
					183,
					193,
					194,
					195,
					196,
					197,
					198,
					209,
					210,
					211,
					212,
					223,
					237,
					238,
					239,
					240,
					241,
					251,
					253,
					254,
					267,
					268,
					269,
					270
					],
			intensities=[
					10,
					10,
					240,
					980,
					30,
					10,
					30,
					180,
					30,
					50,
					90,
					10,
					90,
					100,
					700,
					110,
					30,
					20,
					10,
					20,
					140,
					210,
					400,
					110,
					20,
					10,
					10,
					20,
					20,
					30,
					90,
					3830,
					410,
					160,
					30,
					10,
					20,
					70,
					470,
					1140,
					700,
					90,
					10,
					20,
					200,
					1120,
					650,
					480,
					40,
					10,
					10,
					50,
					340,
					410,
					9999,
					1300,
					100,
					10,
					10,
					10,
					10,
					10,
					30,
					10,
					60,
					20,
					10,
					10,
					10,
					10,
					20,
					7889,
					940,
					70,
					10,
					20,
					10,
					10,
					180,
					1010,
					110,
					30,
					60,
					40,
					10,
					110,
					20,
					10,
					10,
					30,
					30,
					190,
					30,
					10,
					10,
					30,
					130,
					60,
					10,
					10,
					20,
					40,
					10,
					20,
					10,
					10,
					170,
					30,
					10,
					10,
					70,
					10,
					290,
					2940,
					590,
					60
					]
			)

	dpa_similarity = SpectrumSimilarity(diphenylamine, diphenylamine)
	assert dpa_similarity.score()[0] >= 0.99
	dpa_similarity.print_alignment()
	dpa_similarity.plot("before", "after")

	ec_similarity = SpectrumSimilarity(ethyl_centralite, ethyl_centralite)
	assert ec_similarity.score()[0] >= 0.99
	ec_similarity.print_alignment()
	ec_similarity.plot("before", "after")


# test_spectrum_similarity()

#!/usr/bin/env python3
"""
Auto-generated ColabFold batch submission script.

Generated from CKD GWAS pipeline.
Total jobs: 100
"""

import json
from pathlib import Path

JOBS = [
  {
    "protein_id": "UNK_rs12894354",
    "mutation": "Phe295Leu",
    "effect": "LOCUS_72"
  },
  {
    "protein_id": "UNK_rs10790454",
    "mutation": "Ile206Leu",
    "effect": "LOCUS_37"
  },
  {
    "protein_id": "UNK_rs4442348",
    "mutation": "Ile906Val",
    "effect": "LOCUS_151"
  },
  {
    "protein_id": "UNK_rs223317",
    "mutation": "Phe942Leu",
    "effect": "LOCUS_250"
  },
  {
    "protein_id": "UNK_rs1407040",
    "mutation": "Phe392Leu",
    "effect": "LOCUS_174"
  },
  {
    "protein_id": "UNK_rs2034899",
    "mutation": "Phe397Val",
    "effect": "LOCUS_262"
  },
  {
    "protein_id": "UNK_rs293736",
    "mutation": "Ile730Leu",
    "effect": "LOCUS_168"
  },
  {
    "protein_id": "UNK_rs62491533",
    "mutation": "Phe45Leu",
    "effect": "LOCUS_303"
  },
  {
    "protein_id": "UNK_rs1913641",
    "mutation": "Phe414Val",
    "effect": "LOCUS_312"
  },
  {
    "protein_id": "UNK_rs12148280",
    "mutation": "Ile609Val",
    "effect": "LOCUS_77"
  },
  {
    "protein_id": "UNK_rs12448902",
    "mutation": "Leu731Val",
    "effect": "LOCUS_89"
  },
  {
    "protein_id": "UNK_rs61311941",
    "mutation": "Ile775Val",
    "effect": "LOCUS_324"
  },
  {
    "protein_id": "UNK_rs3814995",
    "mutation": "Phe71Leu",
    "effect": "LOCUS_121"
  },
  {
    "protein_id": "UNK_rs10040082",
    "mutation": "Phe285Leu",
    "effect": "LOCUS_259"
  },
  {
    "protein_id": "UNK_rs62325228",
    "mutation": "Phe251Val",
    "effect": "LOCUS_247"
  },
  {
    "protein_id": "UNK_rs10797427",
    "mutation": "Phe911Leu",
    "effect": "LOCUS_128"
  },
  {
    "protein_id": "UNK_rs417237",
    "mutation": "Phe399Val",
    "effect": "LOCUS_164"
  },
  {
    "protein_id": "UNK_rs78444298",
    "mutation": "Ile367Val",
    "effect": "LOCUS_156"
  },
  {
    "protein_id": "UNK_rs60980181",
    "mutation": "Ile856Phe",
    "effect": "LOCUS_212"
  },
  {
    "protein_id": "UNK_rs62035088",
    "mutation": "Ile281Val",
    "effect": "LOCUS_83"
  },
  {
    "protein_id": "UNK_rs807624",
    "mutation": "Phe824Val",
    "effect": "LOCUS_188"
  },
  {
    "protein_id": "UNK_rs34950020",
    "mutation": "Ile182Val",
    "effect": "LOCUS_283"
  },
  {
    "protein_id": "UNK_rs80138475",
    "mutation": "Phe331Leu",
    "effect": "LOCUS_260"
  },
  {
    "protein_id": "UNK_rs28910285",
    "mutation": "Phe329Leu",
    "effect": "LOCUS_184"
  },
  {
    "protein_id": "UNK_rs836968",
    "mutation": "Phe779Leu",
    "effect": "LOCUS_45"
  },
  {
    "protein_id": "UNK_rs10821905",
    "mutation": "Ile698Val",
    "effect": "LOCUS_5"
  },
  {
    "protein_id": "UNK_rs154656",
    "mutation": "Ile668Phe",
    "effect": "LOCUS_97"
  },
  {
    "protein_id": "UNK_rs9465741",
    "mutation": "Ile478Leu",
    "effect": "LOCUS_270"
  },
  {
    "protein_id": "UNK_rs1321917",
    "mutation": "Leu977Val",
    "effect": "LOCUS_326"
  },
  {
    "protein_id": "UNK_rs13159523",
    "mutation": "Ile655Val",
    "effect": "LOCUS_256"
  },
  {
    "protein_id": "UNK_rs7620706",
    "mutation": "Ile586Phe",
    "effect": "LOCUS_227"
  },
  {
    "protein_id": "UNK_rs10827421",
    "mutation": "Phe556Leu",
    "effect": "LOCUS_3"
  },
  {
    "protein_id": "UNK_rs227731",
    "mutation": "Phe747Val",
    "effect": "LOCUS_105"
  },
  {
    "protein_id": "UNK_rs755865",
    "mutation": "Ile645Val",
    "effect": "LOCUS_202"
  },
  {
    "protein_id": "UNK_rs956006",
    "mutation": "Phe180Leu",
    "effect": "LOCUS_78"
  },
  {
    "protein_id": "UNK_rs2241358",
    "mutation": "Leu826Val",
    "effect": "LOCUS_117"
  },
  {
    "protein_id": "UNK_rs1042752",
    "mutation": "Ile371Val",
    "effect": "LOCUS_34"
  },
  {
    "protein_id": "UNK_rs35915570",
    "mutation": "Phe786Leu",
    "effect": "LOCUS_102"
  },
  {
    "protein_id": "UNK_rs59343080",
    "mutation": "Ile225Phe",
    "effect": "LOCUS_124"
  },
  {
    "protein_id": "UNK_rs55924910",
    "mutation": "Leu789Val",
    "effect": "LOCUS_198"
  },
  {
    "protein_id": "UNK_rs12061708",
    "mutation": "Ile973Val",
    "effect": "LOCUS_130"
  },
  {
    "protein_id": "UNK_rs41284816",
    "mutation": "Phe330Val",
    "effect": "LOCUS_58"
  },
  {
    "protein_id": "UNK_rs28735420",
    "mutation": "Phe655Val",
    "effect": "LOCUS_99"
  },
  {
    "protein_id": "UNK_rs7536433",
    "mutation": "Phe725Leu",
    "effect": "LOCUS_141"
  },
  {
    "protein_id": "UNK_rs429358",
    "mutation": "Phe314Leu",
    "effect": "LOCUS_125"
  },
  {
    "protein_id": "UNK_rs2096551",
    "mutation": "Leu867Val",
    "effect": "LOCUS_314"
  },
  {
    "protein_id": "UNK_rs7137828",
    "mutation": "Phe934Leu",
    "effect": "LOCUS_52"
  },
  {
    "protein_id": "UNK_rs3794991",
    "mutation": "Phe866Leu",
    "effect": "LOCUS_119"
  },
  {
    "protein_id": "UNK_rs11071738",
    "mutation": "Phe386Leu",
    "effect": "LOCUS_79"
  },
  {
    "protein_id": "UNK_rs59860440",
    "mutation": "Phe536Leu",
    "effect": "LOCUS_299"
  },
  {
    "protein_id": "UNK_rs1275609",
    "mutation": "Ile728Val",
    "effect": "LOCUS_50"
  },
  {
    "protein_id": "UNK_rs3795503",
    "mutation": "Phe899Leu",
    "effect": "LOCUS_154"
  },
  {
    "protein_id": "UNK_rs7169629",
    "mutation": "Leu92Val",
    "effect": "LOCUS_85"
  },
  {
    "protein_id": "UNK_rs1087289",
    "mutation": "Phe44Val",
    "effect": "LOCUS_271"
  },
  {
    "protein_id": "UNK_rs7005025",
    "mutation": "Ile606Leu",
    "effect": "LOCUS_308"
  },
  {
    "protein_id": "UNK_rs11786896",
    "mutation": "Phe452Leu",
    "effect": "LOCUS_320"
  },
  {
    "protein_id": "UNK_rs112175548",
    "mutation": "Phe14Leu",
    "effect": "LOCUS_94"
  },
  {
    "protein_id": "UNK_rs12826808",
    "mutation": "Ile794Phe",
    "effect": "LOCUS_43"
  },
  {
    "protein_id": "UNK_rs10283362",
    "mutation": "Phe654Leu",
    "effect": "LOCUS_319"
  },
  {
    "protein_id": "UNK_rs151245",
    "mutation": "Phe684Val",
    "effect": "LOCUS_111"
  },
  {
    "protein_id": "UNK_rs132639",
    "mutation": "Ile300Phe",
    "effect": "LOCUS_181"
  },
  {
    "protein_id": "UNK_rs6458868",
    "mutation": "Phe385Leu",
    "effect": "LOCUS_277"
  },
  {
    "protein_id": "UNK_rs7514579",
    "mutation": "Ile451Leu",
    "effect": "LOCUS_143"
  },
  {
    "protein_id": "UNK_rs35072105",
    "mutation": "Ile940Val",
    "effect": "LOCUS_296"
  },
  {
    "protein_id": "UNK_rs34357137",
    "mutation": "Leu681Val",
    "effect": "LOCUS_274"
  },
  {
    "protein_id": "UNK_rs72912510",
    "mutation": "Ile589Val",
    "effect": "LOCUS_278"
  },
  {
    "protein_id": "UNK_rs4275190",
    "mutation": "Phe463Leu",
    "effect": "LOCUS_295"
  },
  {
    "protein_id": "UNK_rs73077077",
    "mutation": "Ile617Val",
    "effect": "LOCUS_167"
  },
  {
    "protein_id": "UNK_rs7492724",
    "mutation": "Ile785Val",
    "effect": "LOCUS_64"
  },
  {
    "protein_id": "UNK_rs1801251",
    "mutation": "Ile821Val",
    "effect": "LOCUS_220"
  },
  {
    "protein_id": "UNK_rs34442537",
    "mutation": "Leu132Val",
    "effect": "LOCUS_254"
  },
  {
    "protein_id": "UNK_rs10746942",
    "mutation": "Ile489Val",
    "effect": "LOCUS_323"
  },
  {
    "protein_id": "UNK_rs73073442",
    "mutation": "Phe430Leu",
    "effect": "LOCUS_290"
  },
  {
    "protein_id": "UNK_rs2823139",
    "mutation": "Ile595Val",
    "effect": "LOCUS_177"
  },
  {
    "protein_id": "UNK_rs9397738",
    "mutation": "Ile222Val",
    "effect": "LOCUS_284"
  },
  {
    "protein_id": "UNK_rs10419627",
    "mutation": "Ile560Val",
    "effect": "LOCUS_116"
  },
  {
    "protein_id": "UNK_rs12152266",
    "mutation": "Phe121Leu",
    "effect": "LOCUS_241"
  },
  {
    "protein_id": "UNK_rs7248248",
    "mutation": "Ile993Phe",
    "effect": "LOCUS_123"
  },
  {
    "protein_id": "UNK_rs10892358",
    "mutation": "Ile932Val",
    "effect": "LOCUS_36"
  },
  {
    "protein_id": "UNK_rs34460334",
    "mutation": "Phe694Leu",
    "effect": "LOCUS_132"
  },
  {
    "protein_id": "UNK_rs2953516",
    "mutation": "Phe849Leu",
    "effect": "LOCUS_313"
  },
  {
    "protein_id": "UNK_rs1858800",
    "mutation": "Phe426Leu",
    "effect": "LOCUS_95"
  },
  {
    "protein_id": "UNK_rs7027509",
    "mutation": "Phe626Leu",
    "effect": "LOCUS_328"
  },
  {
    "protein_id": "UNK_rs9590675",
    "mutation": "Phe731Val",
    "effect": "LOCUS_56"
  },
  {
    "protein_id": "UNK_rs7475348",
    "mutation": "Phe726Leu",
    "effect": "LOCUS_7"
  },
  {
    "protein_id": "UNK_rs267738",
    "mutation": "Phe542Val",
    "effect": "LOCUS_149"
  },
  {
    "protein_id": "UNK_rs264608",
    "mutation": "Phe730Leu",
    "effect": "LOCUS_207"
  },
  {
    "protein_id": "UNK_rs2815374",
    "mutation": "Ile463Val",
    "effect": "LOCUS_140"
  },
  {
    "protein_id": "UNK_rs12907511",
    "mutation": "Leu688Val",
    "effect": "LOCUS_82"
  },
  {
    "protein_id": "UNK_rs736820",
    "mutation": "Ile673Val",
    "effect": "LOCUS_171"
  },
  {
    "protein_id": "UNK_rs10151563",
    "mutation": "Ile702Val",
    "effect": "LOCUS_63"
  },
  {
    "protein_id": "UNK_rs4854645",
    "mutation": "Ile271Val",
    "effect": "LOCUS_232"
  },
  {
    "protein_id": "UNK_rs6708702",
    "mutation": "Ile378Val",
    "effect": "LOCUS_204"
  },
  {
    "protein_id": "UNK_rs11063202",
    "mutation": "Ile231Val",
    "effect": "LOCUS_41"
  },
  {
    "protein_id": "UNK_rs2301343",
    "mutation": "Phe50Val",
    "effect": "LOCUS_192"
  },
  {
    "protein_id": "UNK_rs1719935",
    "mutation": "Ile181Val",
    "effect": "LOCUS_110"
  },
  {
    "protein_id": "UNK_rs4971092",
    "mutation": "Phe649Leu",
    "effect": "LOCUS_150"
  },
  {
    "protein_id": "UNK_rs622076",
    "mutation": "Ile902Val",
    "effect": "LOCUS_272"
  },
  {
    "protein_id": "UNK_rs17602729",
    "mutation": "Ile20Val",
    "effect": "LOCUS_147"
  },
  {
    "protein_id": "UNK_rs112905092",
    "mutation": "Phe409Leu",
    "effect": "LOCUS_214"
  }
]

def main():
    print(f"✓ Loaded {len(JOBS)} ColabFold jobs")
    for i, job in enumerate(JOBS[:5], 1):
        print(f"  [{i}] {job['protein_id']} - {job['mutation']}")
    if len(JOBS) > 5:
        print(f"  ... and {len(JOBS) - 5} more")

if __name__ == "__main__":
    main()

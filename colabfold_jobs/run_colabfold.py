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
    "protein_id": "UNK_rs9823161",
    "mutation": "Ile723Val",
    "effect": "LOCUS_239"
  },
  {
    "protein_id": "UNK_rs836968",
    "mutation": "Phe779Leu",
    "effect": "LOCUS_45"
  },
  {
    "protein_id": "UNK_rs77897671",
    "mutation": "Phe805Leu",
    "effect": "LOCUS_29"
  },
  {
    "protein_id": "UNK_rs7492724",
    "mutation": "Ile785Val",
    "effect": "LOCUS_64"
  },
  {
    "protein_id": "UNK_rs72683923",
    "mutation": "Phe983Leu",
    "effect": "LOCUS_65"
  },
  {
    "protein_id": "UNK_rs10769264",
    "mutation": "Phe781Leu",
    "effect": "LOCUS_26"
  },
  {
    "protein_id": "UNK_rs9649512",
    "mutation": "Ile213Val",
    "effect": "LOCUS_301"
  },
  {
    "protein_id": "UNK_rs4275190",
    "mutation": "Phe463Leu",
    "effect": "LOCUS_295"
  },
  {
    "protein_id": "UNK_rs13157326",
    "mutation": "Ile426Val",
    "effect": "LOCUS_257"
  },
  {
    "protein_id": "UNK_rs4442348",
    "mutation": "Ile906Val",
    "effect": "LOCUS_151"
  },
  {
    "protein_id": "UNK_rs1711667",
    "mutation": "Phe471Val",
    "effect": "LOCUS_17"
  },
  {
    "protein_id": "UNK_rs112905092",
    "mutation": "Phe409Leu",
    "effect": "LOCUS_214"
  },
  {
    "protein_id": "UNK_rs755865",
    "mutation": "Ile645Val",
    "effect": "LOCUS_202"
  },
  {
    "protein_id": "UNK_rs967532",
    "mutation": "Ile144Val",
    "effect": "LOCUS_253"
  },
  {
    "protein_id": "UNK_rs77375846",
    "mutation": "Phe26Leu",
    "effect": "LOCUS_199"
  },
  {
    "protein_id": "UNK_rs10827421",
    "mutation": "Phe556Leu",
    "effect": "LOCUS_3"
  },
  {
    "protein_id": "UNK_rs12024377",
    "mutation": "Ile620Val",
    "effect": "LOCUS_159"
  },
  {
    "protein_id": "UNK_rs4666821",
    "mutation": "Phe752Val",
    "effect": "LOCUS_211"
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
    "protein_id": "UNK_rs4491726",
    "mutation": "Ile426Val",
    "effect": "LOCUS_189"
  },
  {
    "protein_id": "UNK_rs881858",
    "mutation": "Ile204Val",
    "effect": "LOCUS_275"
  },
  {
    "protein_id": "UNK_rs80282103",
    "mutation": "Ile691Phe",
    "effect": "LOCUS_1"
  },
  {
    "protein_id": "UNK_rs7137828",
    "mutation": "Phe934Leu",
    "effect": "LOCUS_52"
  },
  {
    "protein_id": "UNK_rs6481598",
    "mutation": "Leu267Val",
    "effect": "LOCUS_2"
  },
  {
    "protein_id": "UNK_rs11856921",
    "mutation": "Ile703Leu",
    "effect": "LOCUS_73"
  },
  {
    "protein_id": "UNK_rs2815374",
    "mutation": "Ile463Val",
    "effect": "LOCUS_140"
  },
  {
    "protein_id": "UNK_rs1548945",
    "mutation": "Phe263Leu",
    "effect": "LOCUS_215"
  },
  {
    "protein_id": "UNK_rs62435145",
    "mutation": "Phe856Val",
    "effect": "LOCUS_286"
  },
  {
    "protein_id": "UNK_rs3119304",
    "mutation": "Phe853Leu",
    "effect": "LOCUS_285"
  },
  {
    "protein_id": "UNK_rs4854645",
    "mutation": "Ile271Val",
    "effect": "LOCUS_232"
  },
  {
    "protein_id": "UNK_rs807624",
    "mutation": "Phe824Val",
    "effect": "LOCUS_188"
  },
  {
    "protein_id": "UNK_rs7027509",
    "mutation": "Phe626Leu",
    "effect": "LOCUS_328"
  },
  {
    "protein_id": "UNK_rs2158812",
    "mutation": "Phe117Leu",
    "effect": "LOCUS_292"
  },
  {
    "protein_id": "UNK_rs13059257",
    "mutation": "Phe665Leu",
    "effect": "LOCUS_240"
  },
  {
    "protein_id": "UNK_rs4515954",
    "mutation": "Ile823Leu",
    "effect": "LOCUS_28"
  },
  {
    "protein_id": "UNK_rs550057",
    "mutation": "Phe200Leu",
    "effect": "LOCUS_327"
  },
  {
    "protein_id": "UNK_rs72912510",
    "mutation": "Ile589Val",
    "effect": "LOCUS_278"
  },
  {
    "protein_id": "UNK_rs61830291",
    "mutation": "Ile48Leu",
    "effect": "LOCUS_163"
  },
  {
    "protein_id": "UNK_rs17413465",
    "mutation": "Ile903Leu",
    "effect": "LOCUS_138"
  },
  {
    "protein_id": "UNK_rs2781649",
    "mutation": "Ile880Val",
    "effect": "LOCUS_282"
  },
  {
    "protein_id": "UNK_rs73703112",
    "mutation": "Phe515Val",
    "effect": "LOCUS_316"
  },
  {
    "protein_id": "UNK_rs1004441",
    "mutation": "Ile599Val",
    "effect": "LOCUS_187"
  },
  {
    "protein_id": "UNK_rs11676298",
    "mutation": "Leu911Val",
    "effect": "LOCUS_218"
  },
  {
    "protein_id": "UNK_rs10866705",
    "mutation": "Ile711Leu",
    "effect": "LOCUS_267"
  },
  {
    "protein_id": "UNK_rs12575164",
    "mutation": "Phe144Leu",
    "effect": "LOCUS_38"
  },
  {
    "protein_id": "UNK_rs950965",
    "mutation": "Ile770Val",
    "effect": "LOCUS_196"
  },
  {
    "protein_id": "UNK_rs2297129",
    "mutation": "Ile309Val",
    "effect": "LOCUS_68"
  },
  {
    "protein_id": "UNK_rs10797427",
    "mutation": "Phe911Leu",
    "effect": "LOCUS_128"
  },
  {
    "protein_id": "UNK_rs7740107",
    "mutation": "Ile154Phe",
    "effect": "LOCUS_281"
  },
  {
    "protein_id": "UNK_rs10934753",
    "mutation": "Ile727Val",
    "effect": "LOCUS_231"
  },
  {
    "protein_id": "UNK_rs2250067",
    "mutation": "Phe11Leu",
    "effect": "LOCUS_230"
  },
  {
    "protein_id": "UNK_rs11123169",
    "mutation": "Phe26Leu",
    "effect": "LOCUS_200"
  },
  {
    "protein_id": "UNK_rs580114",
    "mutation": "Ile58Val",
    "effect": "LOCUS_133"
  },
  {
    "protein_id": "UNK_rs60980181",
    "mutation": "Ile856Phe",
    "effect": "LOCUS_212"
  },
  {
    "protein_id": "UNK_rs10892358",
    "mutation": "Ile932Val",
    "effect": "LOCUS_36"
  },
  {
    "protein_id": "UNK_rs1858800",
    "mutation": "Phe426Leu",
    "effect": "LOCUS_95"
  },
  {
    "protein_id": "UNK_rs72801857",
    "mutation": "Phe790Leu",
    "effect": "LOCUS_190"
  },
  {
    "protein_id": "UNK_rs11821711",
    "mutation": "Phe567Leu",
    "effect": "LOCUS_27"
  },
  {
    "protein_id": "UNK_rs28910285",
    "mutation": "Phe329Leu",
    "effect": "LOCUS_184"
  },
  {
    "protein_id": "UNK_rs12544197",
    "mutation": "Ile609Val",
    "effect": "LOCUS_315"
  },
  {
    "protein_id": "UNK_rs4970765",
    "mutation": "Phe724Leu",
    "effect": "LOCUS_145"
  },
  {
    "protein_id": "UNK_rs9895661",
    "mutation": "Phe864Leu",
    "effect": "LOCUS_106"
  },
  {
    "protein_id": "UNK_rs12458009",
    "mutation": "Phe503Val",
    "effect": "LOCUS_114"
  },
  {
    "protein_id": "UNK_rs11768336",
    "mutation": "Phe231Leu",
    "effect": "LOCUS_288"
  },
  {
    "protein_id": "UNK_rs1111571",
    "mutation": "Ile728Val",
    "effect": "LOCUS_92"
  },
  {
    "protein_id": "UNK_rs10790454",
    "mutation": "Ile206Leu",
    "effect": "LOCUS_37"
  },
  {
    "protein_id": "UNK_rs7324484",
    "mutation": "Ile27Val",
    "effect": "LOCUS_57"
  },
  {
    "protein_id": "UNK_rs73073442",
    "mutation": "Phe430Leu",
    "effect": "LOCUS_290"
  },
  {
    "protein_id": "UNK_rs4376843",
    "mutation": "Leu363Val",
    "effect": "LOCUS_8"
  },
  {
    "protein_id": "UNK_rs9932625",
    "mutation": "Ile249Val",
    "effect": "LOCUS_90"
  },
  {
    "protein_id": "UNK_rs8101667",
    "mutation": "Phe140Leu",
    "effect": "LOCUS_120"
  },
  {
    "protein_id": "UNK_rs11202328",
    "mutation": "Phe64Leu",
    "effect": "LOCUS_10"
  },
  {
    "protein_id": "UNK_rs1407040",
    "mutation": "Phe392Leu",
    "effect": "LOCUS_174"
  },
  {
    "protein_id": "UNK_rs1801251",
    "mutation": "Ile821Val",
    "effect": "LOCUS_220"
  },
  {
    "protein_id": "UNK_rs2034899",
    "mutation": "Phe397Val",
    "effect": "LOCUS_262"
  },
  {
    "protein_id": "UNK_rs11170624",
    "mutation": "Phe80Val",
    "effect": "LOCUS_48"
  },
  {
    "protein_id": "UNK_rs1087289",
    "mutation": "Phe44Val",
    "effect": "LOCUS_271"
  },
  {
    "protein_id": "UNK_rs10283362",
    "mutation": "Phe654Leu",
    "effect": "LOCUS_319"
  },
  {
    "protein_id": "UNK_rs62035088",
    "mutation": "Ile281Val",
    "effect": "LOCUS_83"
  },
  {
    "protein_id": "UNK_rs4245230",
    "mutation": "Ile889Val",
    "effect": "LOCUS_113"
  },
  {
    "protein_id": "UNK_rs75625374",
    "mutation": "Leu478Val",
    "effect": "LOCUS_161"
  },
  {
    "protein_id": "UNK_rs73077077",
    "mutation": "Ile617Val",
    "effect": "LOCUS_167"
  },
  {
    "protein_id": "UNK_rs2306623",
    "mutation": "Phe977Leu",
    "effect": "LOCUS_223"
  },
  {
    "protein_id": "UNK_rs3775932",
    "mutation": "Ile644Leu",
    "effect": "LOCUS_243"
  },
  {
    "protein_id": "UNK_rs7326821",
    "mutation": "Ile735Val",
    "effect": "LOCUS_61"
  },
  {
    "protein_id": "UNK_rs264608",
    "mutation": "Phe730Leu",
    "effect": "LOCUS_207"
  },
  {
    "protein_id": "UNK_rs3795503",
    "mutation": "Phe899Leu",
    "effect": "LOCUS_154"
  },
  {
    "protein_id": "UNK_rs2954017",
    "mutation": "Phe958Leu",
    "effect": "LOCUS_317"
  },
  {
    "protein_id": "UNK_rs429358",
    "mutation": "Phe314Leu",
    "effect": "LOCUS_125"
  },
  {
    "protein_id": "UNK_rs55658481",
    "mutation": "Ile739Val",
    "effect": "LOCUS_216"
  },
  {
    "protein_id": "UNK_rs146192644",
    "mutation": "Ile31Leu",
    "effect": "LOCUS_264"
  },
  {
    "protein_id": "UNK_rs7514579",
    "mutation": "Ile451Leu",
    "effect": "LOCUS_143"
  },
  {
    "protein_id": "UNK_rs7475348",
    "mutation": "Phe726Leu",
    "effect": "LOCUS_7"
  },
  {
    "protein_id": "UNK_rs9812319",
    "mutation": "Phe954Leu",
    "effect": "LOCUS_233"
  },
  {
    "protein_id": "UNK_rs34442537",
    "mutation": "Leu132Val",
    "effect": "LOCUS_254"
  },
  {
    "protein_id": "UNK_rs2433601",
    "mutation": "Phe809Leu",
    "effect": "LOCUS_75"
  },
  {
    "protein_id": "UNK_rs12212034",
    "mutation": "Phe288Leu",
    "effect": "LOCUS_276"
  },
  {
    "protein_id": "UNK_rs6968865",
    "mutation": "Ile424Phe",
    "effect": "LOCUS_287"
  },
  {
    "protein_id": "UNK_rs16930370",
    "mutation": "Phe233Leu",
    "effect": "LOCUS_40"
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

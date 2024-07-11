

<!-- README.md is generated from README.qmd. Please edit that file -->

# Twitter Data

This repository contains Twitter data for selected political figures.

![**Wordcloud of Abiy Ahmed’s tweets**](doc/fig-wordcloud-output-1.png)

<details>
<summary>
List of people/org
</summary>

| Account                                          |
|:-------------------------------------------------|
| [abiyahmedali](https://x.com/abiyahmedali)       |
| [reda_getachew](https://x.com/reda_getachew)     |
| [PMEthiopia](https://x.com/PMEthiopia)           |
| [DrTedros](https://x.com/DrTedros)               |
| [fitsumaregaa](https://x.com/fitsumaregaa)       |
| [seleshi_b_a](https://x.com/seleshi_b_a)         |
| [ShimelisAbdisa](https://x.com/ShimelisAbdisa)   |
| [yilkal_kefale](https://x.com/yilkal_kefale)     |
| [AgegnehuT](https://x.com/AgegnehuT)             |
| [GeduAndargachew](https://x.com/GeduAndargachew) |
| [TirunehDinku](https://x.com/TirunehDinku)       |
| [AdanechAbiebie](https://x.com/AdanechAbiebie)   |
| [RedwanHussien](https://x.com/RedwanHussien)     |
| [AAA_Amhara](https://x.com/AAA_Amhara)           |
| [TakeleUma](https://x.com/TakeleUma)             |
| [EthioHRC](https://x.com/EthioHRC)               |
| [DanielBekele](https://x.com/DanielBekele)       |
| [BilleneSeyoum](https://x.com/BilleneSeyoum)     |
| [FdreService](https://x.com/FdreService)         |
| [DemekeHasen](https://x.com/DemekeHasen)         |
| [SahleWorkZewde](https://x.com/SahleWorkZewde)   |
| [mfaethiopia](https://x.com/mfaethiopia)         |
| [FLEthiopia](https://x.com/FLEthiopia)           |
| [ashenafi_meaza](https://x.com/ashenafi_meaza)   |
| [AregaKitessa](https://x.com/AregaKitessa)       |
| [AMECOONLINE](https://x.com/AMECOONLINE)         |
| [FMoHealth](https://x.com/FMoHealth)             |
| [fdremoe](https://x.com/fdremoe)                 |
| [fanatelevision](https://x.com/fanatelevision)   |
| [addisstandard](https://x.com/addisstandard)     |
| [MoF_Ethiopia](https://x.com/MoF_Ethiopia)       |
| [MoP_Ethiopia](https://x.com/MoP_Ethiopia)       |
| [BerhanuTsegaye](https://x.com/BerhanuTsegaye)   |
| [ebczena](https://x.com/ebczena)                 |
| [ethiotelecom](https://x.com/ethiotelecom)       |
| [TayeAtske](https://x.com/TayeAtske)             |
| [ETHZema](https://x.com/ETHZema)                 |
| [EA_DevCouncil](https://x.com/EA_DevCouncil)     |
| [lia_tadesse](https://x.com/lia_tadesse)         |
| [cdessalegn](https://x.com/cdessalegn)           |
| [NAMA_at_ABIN](https://x.com/NAMA_at_ABIN)       |
| [VOAAmharic](https://x.com/VOAAmharic)           |
| [EthiopianNewsA](https://x.com/EthiopianNewsA)   |
| [GPEthiopia](https://x.com/GPEthiopia)           |
| [MARHEIR_GEBRYE](https://x.com/MARHEIR_GEBRYE)   |
| [AndargachewTse2](https://x.com/AndargachewTse2) |
| [dw_amharic](https://x.com/dw_amharic)           |
| [eskinder_nega](https://x.com/eskinder_nega)     |
| [danielkibret](https://x.com/danielkibret)       |
| [walta_info](https://x.com/walta_info)           |
| [Mustafe_M_Omer](https://x.com/Mustafe_M_Omer)   |
| [dagmawit_moges](https://x.com/dagmawit_moges)   |
| [BeleteMG](https://x.com/BeleteMG)               |
| [ETFactCheck](https://x.com/ETFactCheck)         |

</details>

## Requirements

1.  `python` 3.12

    ``` sh
    uv pip install -r requirements.txt
    ```

    <!-- 2. `r` 4.4 -->

2.  `quarto`

## Usage

You can generate `analyze_tweets.html` for each handle. For example, for
handle “reda_getachew” run

``` sh
quarto render analyze_tweets.qmd -P handle:reda_getachew
```

- `data/twitter-data/` contains data from the Twitter API (before the
  recent X fiasco).
- `data/apify/` contains latest (until 2024-07-10) data scraped using an
  Apify actor [Twitter
  Scraper](https://apify.com/microworlds/twitter-scraper), which
  requires dropping some [coins](doc/twitter-scraper.jpeg) (\$). Please
  consider starring this repository.

## Contribution

Please analyze the data and uncover subtle insights. Share your
analysis.

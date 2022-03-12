# empire_earth

[![Documentation Status](https://readthedocs.org/projects/empire-earth/badge/?version=latest)](https://empire-earth.readthedocs.io/en/latest/?badge=latest)

Utilites for calculating strategies in Empire Earth.

<div class="cell_output docutils container">
<div class="output text_html"><style type="text/css">
#T_a40eb thead tr th:nth-child(1) {
  position: sticky;
  background-color: white;
  left: 0px;
  z-index: 3 !important;
}
#T_a40eb tbody tr th:nth-child(1) {
  position: sticky;
  background-color: white;
  left: 0px;
  z-index: 1;
}
#T_a40eb_row0_col0, #T_a40eb_row0_col1, #T_a40eb_row1_col0, #T_a40eb_row1_col1, #T_a40eb_row2_col2, #T_a40eb_row3_col3, #T_a40eb_row4_col4, #T_a40eb_row5_col5, #T_a40eb_row7_col7, #T_a40eb_row8_col8, #T_a40eb_row9_col9, #T_a40eb_row10_col10, #T_a40eb_row11_col11, #T_a40eb_row12_col12, #T_a40eb_row13_col13 {
  background-color: #fefeff;
  color: #000000;
}
#T_a40eb_row0_col2, #T_a40eb_row1_col2, #T_a40eb_row5_col7 {
  background-color: #ff7474;
  color: #f1f1f1;
}
#T_a40eb_row0_col3, #T_a40eb_row1_col3 {
  background-color: #ffb4b4;
  color: #000000;
}
#T_a40eb_row0_col4, #T_a40eb_row1_col4, #T_a40eb_row8_col13, #T_a40eb_row12_col11 {
  background-color: #ffcaca;
  color: #000000;
}
#T_a40eb_row0_col5, #T_a40eb_row1_col5 {
  background-color: #ff7272;
  color: #f1f1f1;
}
#T_a40eb_row0_col6, #T_a40eb_row1_col6, #T_a40eb_row2_col6, #T_a40eb_row3_col6, #T_a40eb_row4_col6, #T_a40eb_row5_col6, #T_a40eb_row7_col0, #T_a40eb_row7_col1, #T_a40eb_row7_col4, #T_a40eb_row9_col6, #T_a40eb_row10_col6, #T_a40eb_row11_col4, #T_a40eb_row11_col6, #T_a40eb_row12_col6, #T_a40eb_row13_col0, #T_a40eb_row13_col1, #T_a40eb_row13_col6 {
  background-color: #0000ff;
  color: #f1f1f1;
}
#T_a40eb_row0_col7, #T_a40eb_row0_col13, #T_a40eb_row1_col7, #T_a40eb_row1_col13, #T_a40eb_row4_col7, #T_a40eb_row4_col11, #T_a40eb_row6_col0, #T_a40eb_row6_col1, #T_a40eb_row6_col2, #T_a40eb_row6_col3, #T_a40eb_row6_col4, #T_a40eb_row6_col5, #T_a40eb_row6_col9, #T_a40eb_row6_col10, #T_a40eb_row6_col11, #T_a40eb_row6_col12, #T_a40eb_row6_col13 {
  background-color: #ff0000;
  color: #f1f1f1;
}
#T_a40eb_row0_col8, #T_a40eb_row1_col8 {
  background-color: #ff1a1a;
  color: #f1f1f1;
}
#T_a40eb_row0_col9, #T_a40eb_row1_col9, #T_a40eb_row3_col10, #T_a40eb_row12_col13 {
  background-color: #ffa8a8;
  color: #000000;
}
#T_a40eb_row0_col10, #T_a40eb_row1_col10 {
  background-color: #ff7a7a;
  color: #f1f1f1;
}
#T_a40eb_row0_col11, #T_a40eb_row1_col11 {
  background-color: #ff1818;
  color: #f1f1f1;
}
#T_a40eb_row0_col12, #T_a40eb_row1_col12, #T_a40eb_row2_col7 {
  background-color: #ff3c3c;
  color: #f1f1f1;
}
#T_a40eb_row2_col0, #T_a40eb_row2_col1, #T_a40eb_row7_col5 {
  background-color: #7474ff;
  color: #f1f1f1;
}
#T_a40eb_row2_col3, #T_a40eb_row9_col11 {
  background-color: #fff6f6;
  color: #000000;
}
#T_a40eb_row2_col4 {
  background-color: #9a9aff;
  color: #f1f1f1;
}
#T_a40eb_row2_col5 {
  background-color: #ffd6d6;
  color: #000000;
}
#T_a40eb_row2_col8 {
  background-color: #ff6e6e;
  color: #f1f1f1;
}
#T_a40eb_row2_col9 {
  background-color: #ffe4e4;
  color: #000000;
}
#T_a40eb_row2_col10, #T_a40eb_row6_col7, #T_a40eb_row11_col13, #T_a40eb_row12_col8 {
  background-color: #ffdcdc;
  color: #000000;
}
#T_a40eb_row2_col11, #T_a40eb_row9_col12, #T_a40eb_row10_col8 {
  background-color: #ff6c6c;
  color: #f1f1f1;
}
#T_a40eb_row2_col12 {
  background-color: #ff8a8a;
  color: #000000;
}
#T_a40eb_row2_col13 {
  background-color: #ff3232;
  color: #f1f1f1;
}
#T_a40eb_row3_col0, #T_a40eb_row3_col1 {
  background-color: #b4b4ff;
  color: #000000;
}
#T_a40eb_row3_col2, #T_a40eb_row11_col9 {
  background-color: #f6f6ff;
  color: #000000;
}
#T_a40eb_row3_col4 {
  background-color: #fff2f2;
  color: #000000;
}
#T_a40eb_row3_col5 {
  background-color: #ffeeee;
  color: #000000;
}
#T_a40eb_row3_col7 {
  background-color: #ff3434;
  color: #f1f1f1;
}
#T_a40eb_row3_col8, #T_a40eb_row9_col7 {
  background-color: #ff6666;
  color: #f1f1f1;
}
#T_a40eb_row3_col9 {
  background-color: #ffcece;
  color: #000000;
}
#T_a40eb_row3_col11 {
  background-color: #ff3838;
  color: #f1f1f1;
}
#T_a40eb_row3_col12 {
  background-color: #ff8080;
  color: #f1f1f1;
}
#T_a40eb_row3_col13 {
  background-color: #ff2828;
  color: #f1f1f1;
}
#T_a40eb_row4_col0, #T_a40eb_row4_col1, #T_a40eb_row11_col12, #T_a40eb_row13_col8 {
  background-color: #cacaff;
  color: #000000;
}
#T_a40eb_row4_col2 {
  background-color: #ff9a9a;
  color: #000000;
}
#T_a40eb_row4_col3 {
  background-color: #f2f2ff;
  color: #000000;
}
#T_a40eb_row4_col5 {
  background-color: #ff5454;
  color: #f1f1f1;
}
#T_a40eb_row4_col8 {
  background-color: #ff0202;
  color: #f1f1f1;
}
#T_a40eb_row4_col9 {
  background-color: #ffb8b8;
  color: #000000;
}
#T_a40eb_row4_col10 {
  background-color: #ff4c4c;
  color: #f1f1f1;
}
#T_a40eb_row4_col12 {
  background-color: #ff6868;
  color: #f1f1f1;
}
#T_a40eb_row4_col13 {
  background-color: #ff1212;
  color: #f1f1f1;
}
#T_a40eb_row5_col0, #T_a40eb_row5_col1 {
  background-color: #7272ff;
  color: #f1f1f1;
}
#T_a40eb_row5_col2 {
  background-color: #d6d6ff;
  color: #000000;
}
#T_a40eb_row5_col3 {
  background-color: #eeeeff;
  color: #000000;
}
#T_a40eb_row5_col4 {
  background-color: #5454ff;
  color: #f1f1f1;
}
#T_a40eb_row5_col8 {
  background-color: #ffa6a6;
  color: #000000;
}
#T_a40eb_row5_col9, #T_a40eb_row6_col8 {
  background-color: #f0f0ff;
  color: #000000;
}
#T_a40eb_row5_col10 {
  background-color: #f8f8ff;
  color: #000000;
}
#T_a40eb_row5_col11 {
  background-color: #ff9494;
  color: #000000;
}
#T_a40eb_row5_col12, #T_a40eb_row10_col12 {
  background-color: #ffc2c2;
  color: #000000;
}
#T_a40eb_row5_col13, #T_a40eb_row10_col13 {
  background-color: #ff6a6a;
  color: #f1f1f1;
}
#T_a40eb_row6_col6 {
  background-color: #000000;
  color: #f1f1f1;
}
#T_a40eb_row7_col2, #T_a40eb_row12_col0, #T_a40eb_row12_col1 {
  background-color: #3c3cff;
  color: #f1f1f1;
}
#T_a40eb_row7_col3 {
  background-color: #3434ff;
  color: #f1f1f1;
}
#T_a40eb_row7_col6, #T_a40eb_row8_col12, #T_a40eb_row10_col2, #T_a40eb_row13_col11 {
  background-color: #dcdcff;
  color: #000000;
}
#T_a40eb_row7_col8 {
  background-color: #ccccff;
  color: #000000;
}
#T_a40eb_row7_col9, #T_a40eb_row8_col3 {
  background-color: #6666ff;
  color: #f1f1f1;
}
#T_a40eb_row7_col10 {
  background-color: #3a3aff;
  color: #f1f1f1;
}
#T_a40eb_row7_col11 {
  background-color: #acacff;
  color: #000000;
}
#T_a40eb_row7_col12 {
  background-color: #aaaaff;
  color: #000000;
}
#T_a40eb_row7_col13 {
  background-color: #fffcfc;
  color: #000000;
}
#T_a40eb_row8_col0, #T_a40eb_row8_col1 {
  background-color: #1a1aff;
  color: #f1f1f1;
}
#T_a40eb_row8_col2 {
  background-color: #6e6eff;
  color: #f1f1f1;
}
#T_a40eb_row8_col4 {
  background-color: #0202ff;
  color: #f1f1f1;
}
#T_a40eb_row8_col5 {
  background-color: #a6a6ff;
  color: #000000;
}
#T_a40eb_row8_col6, #T_a40eb_row9_col5 {
  background-color: #fff0f0;
  color: #000000;
}
#T_a40eb_row8_col7 {
  background-color: #ffcccc;
  color: #000000;
}
#T_a40eb_row8_col9 {
  background-color: #9898ff;
  color: #f1f1f1;
}
#T_a40eb_row8_col10, #T_a40eb_row11_col2, #T_a40eb_row12_col9 {
  background-color: #6c6cff;
  color: #f1f1f1;
}
#T_a40eb_row8_col11 {
  background-color: #dedeff;
  color: #000000;
}
#T_a40eb_row9_col0, #T_a40eb_row9_col1, #T_a40eb_row10_col3, #T_a40eb_row13_col12 {
  background-color: #a8a8ff;
  color: #000000;
}
#T_a40eb_row9_col2 {
  background-color: #e4e4ff;
  color: #000000;
}
#T_a40eb_row9_col3 {
  background-color: #ceceff;
  color: #000000;
}
#T_a40eb_row9_col4 {
  background-color: #b8b8ff;
  color: #000000;
}
#T_a40eb_row9_col8 {
  background-color: #ff9898;
  color: #000000;
}
#T_a40eb_row9_col10 {
  background-color: #ffd0d0;
  color: #000000;
}
#T_a40eb_row9_col13 {
  background-color: #ff1616;
  color: #f1f1f1;
}
#T_a40eb_row10_col0, #T_a40eb_row10_col1 {
  background-color: #7a7aff;
  color: #f1f1f1;
}
#T_a40eb_row10_col4 {
  background-color: #4c4cff;
  color: #f1f1f1;
}
#T_a40eb_row10_col5 {
  background-color: #fff8f8;
  color: #000000;
}
#T_a40eb_row10_col7 {
  background-color: #ff3a3a;
  color: #f1f1f1;
}
#T_a40eb_row10_col9 {
  background-color: #d0d0ff;
  color: #000000;
}
#T_a40eb_row10_col11 {
  background-color: #ff8e8e;
  color: #000000;
}
#T_a40eb_row11_col0, #T_a40eb_row11_col1 {
  background-color: #1818ff;
  color: #f1f1f1;
}
#T_a40eb_row11_col3 {
  background-color: #3838ff;
  color: #f1f1f1;
}
#T_a40eb_row11_col5 {
  background-color: #9494ff;
  color: #f1f1f1;
}
#T_a40eb_row11_col7 {
  background-color: #ffacac;
  color: #000000;
}
#T_a40eb_row11_col8 {
  background-color: #ffdede;
  color: #000000;
}
#T_a40eb_row11_col10 {
  background-color: #8e8eff;
  color: #f1f1f1;
}
#T_a40eb_row12_col2 {
  background-color: #8a8aff;
  color: #f1f1f1;
}
#T_a40eb_row12_col3 {
  background-color: #8080ff;
  color: #f1f1f1;
}
#T_a40eb_row12_col4 {
  background-color: #6868ff;
  color: #f1f1f1;
}
#T_a40eb_row12_col5, #T_a40eb_row12_col10 {
  background-color: #c2c2ff;
  color: #000000;
}
#T_a40eb_row12_col7 {
  background-color: #ffaaaa;
  color: #000000;
}
#T_a40eb_row13_col2 {
  background-color: #3232ff;
  color: #f1f1f1;
}
#T_a40eb_row13_col3 {
  background-color: #2828ff;
  color: #f1f1f1;
}
#T_a40eb_row13_col4 {
  background-color: #1212ff;
  color: #f1f1f1;
}
#T_a40eb_row13_col5, #T_a40eb_row13_col10 {
  background-color: #6a6aff;
  color: #f1f1f1;
}
#T_a40eb_row13_col7 {
  background-color: #fcfcff;
  color: #000000;
}
#T_a40eb_row13_col9 {
  background-color: #1616ff;
  color: #f1f1f1;
}
</style>
<table id="T_a40eb">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_a40eb_level0_col0" class="col_heading level0 col0" >Citizen</th>
      <th id="T_a40eb_level0_col1" class="col_heading level0 col1" >Female Citizen</th>
      <th id="T_a40eb_level0_col2" class="col_heading level0 col2" >Maceman</th>
      <th id="T_a40eb_level0_col3" class="col_heading level0 col3" >Spearman</th>
      <th id="T_a40eb_level0_col4" class="col_heading level0 col4" >Simple Bowman</th>
      <th id="T_a40eb_level0_col5" class="col_heading level0 col5" >Horseman</th>
      <th id="T_a40eb_level0_col6" class="col_heading level0 col6" >Sampson</th>
      <th id="T_a40eb_level0_col7" class="col_heading level0 col7" >Tower - Copper</th>
      <th id="T_a40eb_level0_col8" class="col_heading level0 col8" >Tower - Palisades</th>
      <th id="T_a40eb_level0_col9" class="col_heading level0 col9" >Galley - Copper</th>
      <th id="T_a40eb_level0_col10" class="col_heading level0 col10" >Frigate - Copper</th>
      <th id="T_a40eb_level0_col11" class="col_heading level0 col11" >Battleship - Copper</th>
      <th id="T_a40eb_level0_col12" class="col_heading level0 col12" >Sargon of Akkad</th>
      <th id="T_a40eb_level0_col13" class="col_heading level0 col13" >Gilgamesh</th>
    </tr>
    <tr>
      <th class="index_name level0" >Attacker</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
      <th class="blank col8" >&nbsp;</th>
      <th class="blank col9" >&nbsp;</th>
      <th class="blank col10" >&nbsp;</th>
      <th class="blank col11" >&nbsp;</th>
      <th class="blank col12" >&nbsp;</th>
      <th class="blank col13" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_a40eb_level0_row0" class="row_heading level0 row0" >Citizen</th>
      <td id="T_a40eb_row0_col0" class="data row0 col0" >1.000000</td>
      <td id="T_a40eb_row0_col1" class="data row0 col1" >1.000000</td>
      <td id="T_a40eb_row0_col2" class="data row0 col2" >0.083333</td>
      <td id="T_a40eb_row0_col3" class="data row0 col3" >0.254902</td>
      <td id="T_a40eb_row0_col4" class="data row0 col4" >0.380117</td>
      <td id="T_a40eb_row0_col5" class="data row0 col5" >0.079657</td>
      <td id="T_a40eb_row0_col6" class="data row0 col6" >inf</td>
      <td id="T_a40eb_row0_col7" class="data row0 col7" >0.006592</td>
      <td id="T_a40eb_row0_col8" class="data row0 col8" >0.016250</td>
      <td id="T_a40eb_row0_col9" class="data row0 col9" >0.208333</td>
      <td id="T_a40eb_row0_col10" class="data row0 col10" >0.090278</td>
      <td id="T_a40eb_row0_col11" class="data row0 col11" >0.015532</td>
      <td id="T_a40eb_row0_col12" class="data row0 col12" >0.030093</td>
      <td id="T_a40eb_row0_col13" class="data row0 col13" >0.006217</td>
    </tr>
    <tr>
      <th id="T_a40eb_level0_row1" class="row_heading level0 row1" >Female Citizen</th>
      <td id="T_a40eb_row1_col0" class="data row1 col0" >1.000000</td>
      <td id="T_a40eb_row1_col1" class="data row1 col1" >1.000000</td>
      <td id="T_a40eb_row1_col2" class="data row1 col2" >0.083333</td>
      <td id="T_a40eb_row1_col3" class="data row1 col3" >0.254902</td>
      <td id="T_a40eb_row1_col4" class="data row1 col4" >0.380117</td>
      <td id="T_a40eb_row1_col5" class="data row1 col5" >0.079657</td>
      <td id="T_a40eb_row1_col6" class="data row1 col6" >inf</td>
      <td id="T_a40eb_row1_col7" class="data row1 col7" >0.006592</td>
      <td id="T_a40eb_row1_col8" class="data row1 col8" >0.016250</td>
      <td id="T_a40eb_row1_col9" class="data row1 col9" >0.208333</td>
      <td id="T_a40eb_row1_col10" class="data row1 col10" >0.090278</td>
      <td id="T_a40eb_row1_col11" class="data row1 col11" >0.015532</td>
      <td id="T_a40eb_row1_col12" class="data row1 col12" >0.030093</td>
      <td id="T_a40eb_row1_col13" class="data row1 col13" >0.006217</td>
    </tr>
    <tr>
      <th id="T_a40eb_level0_row2" class="row_heading level0 row2" >Maceman</th>
      <td id="T_a40eb_row2_col0" class="data row2 col0" >12.000000</td>
      <td id="T_a40eb_row2_col1" class="data row2 col1" >12.000000</td>
      <td id="T_a40eb_row2_col2" class="data row2 col2" >1.000000</td>
      <td id="T_a40eb_row2_col3" class="data row2 col3" >0.862745</td>
      <td id="T_a40eb_row2_col4" class="data row2 col4" >6.157895</td>
      <td id="T_a40eb_row2_col5" class="data row2 col5" >0.477941</td>
      <td id="T_a40eb_row2_col6" class="data row2 col6" >inf</td>
      <td id="T_a40eb_row2_col7" class="data row2 col7" >0.029665</td>
      <td id="T_a40eb_row2_col8" class="data row2 col8" >0.073125</td>
      <td id="T_a40eb_row2_col9" class="data row2 col9" >0.625000</td>
      <td id="T_a40eb_row2_col10" class="data row2 col10" >0.541667</td>
      <td id="T_a40eb_row2_col11" class="data row2 col11" >0.069892</td>
      <td id="T_a40eb_row2_col12" class="data row2 col12" >0.122222</td>
      <td id="T_a40eb_row2_col13" class="data row2 col13" >0.025251</td>
    </tr>
    <tr>
      <th id="T_a40eb_level0_row3" class="row_heading level0 row3" >Spearman</th>
      <td id="T_a40eb_row3_col0" class="data row3 col0" >3.923077</td>
      <td id="T_a40eb_row3_col1" class="data row3 col1" >3.923077</td>
      <td id="T_a40eb_row3_col2" class="data row3 col2" >1.159091</td>
      <td id="T_a40eb_row3_col3" class="data row3 col3" >1.000000</td>
      <td id="T_a40eb_row3_col4" class="data row3 col4" >0.795322</td>
      <td id="T_a40eb_row3_col5" class="data row3 col5" >0.743750</td>
      <td id="T_a40eb_row3_col6" class="data row3 col6" >inf</td>
      <td id="T_a40eb_row3_col7" class="data row3 col7" >0.025862</td>
      <td id="T_a40eb_row3_col8" class="data row3 col8" >0.063750</td>
      <td id="T_a40eb_row3_col9" class="data row3 col9" >0.408654</td>
      <td id="T_a40eb_row3_col10" class="data row3 col10" >0.212500</td>
      <td id="T_a40eb_row3_col11" class="data row3 col11" >0.027419</td>
      <td id="T_a40eb_row3_col12" class="data row3 col12" >0.102315</td>
      <td id="T_a40eb_row3_col13" class="data row3 col13" >0.021138</td>
    </tr>
    <tr>
      <th id="T_a40eb_level0_row4" class="row_heading level0 row4" >Simple Bowman</th>
      <td id="T_a40eb_row4_col0" class="data row4 col0" >2.630769</td>
      <td id="T_a40eb_row4_col1" class="data row4 col1" >2.630769</td>
      <td id="T_a40eb_row4_col2" class="data row4 col2" >0.162393</td>
      <td id="T_a40eb_row4_col3" class="data row4 col3" >1.257353</td>
      <td id="T_a40eb_row4_col4" class="data row4 col4" >1.000000</td>
      <td id="T_a40eb_row4_col5" class="data row4 col5" >0.046569</td>
      <td id="T_a40eb_row4_col6" class="data row4 col6" >inf</td>
      <td id="T_a40eb_row4_col7" class="data row4 col7" >0.004336</td>
      <td id="T_a40eb_row4_col8" class="data row4 col8" >0.010687</td>
      <td id="T_a40eb_row4_col9" class="data row4 col9" >0.274038</td>
      <td id="T_a40eb_row4_col10" class="data row4 col10" >0.039583</td>
      <td id="T_a40eb_row4_col11" class="data row4 col11" >0.010215</td>
      <td id="T_a40eb_row4_col12" class="data row4 col12" >0.067292</td>
      <td id="T_a40eb_row4_col13" class="data row4 col13" >0.013902</td>
    </tr>
    <tr>
      <th id="T_a40eb_level0_row5" class="row_heading level0 row5" >Horseman</th>
      <td id="T_a40eb_row5_col0" class="data row5 col0" >12.553846</td>
      <td id="T_a40eb_row5_col1" class="data row5 col1" >12.553846</td>
      <td id="T_a40eb_row5_col2" class="data row5 col2" >2.092308</td>
      <td id="T_a40eb_row5_col3" class="data row5 col3" >1.344538</td>
      <td id="T_a40eb_row5_col4" class="data row5 col4" >21.473684</td>
      <td id="T_a40eb_row5_col5" class="data row5 col5" >1.000000</td>
      <td id="T_a40eb_row5_col6" class="data row5 col6" >inf</td>
      <td id="T_a40eb_row5_col7" class="data row5 col7" >0.082759</td>
      <td id="T_a40eb_row5_col8" class="data row5 col8" >0.204000</td>
      <td id="T_a40eb_row5_col9" class="data row5 col9" >1.307692</td>
      <td id="T_a40eb_row5_col10" class="data row5 col10" >1.133333</td>
      <td id="T_a40eb_row5_col11" class="data row5 col11" >0.146237</td>
      <td id="T_a40eb_row5_col12" class="data row5 col12" >0.333333</td>
      <td id="T_a40eb_row5_col13" class="data row5 col13" >0.068867</td>
    </tr>
    <tr>
      <th id="T_a40eb_level0_row6" class="row_heading level0 row6" >Sampson</th>
      <td id="T_a40eb_row6_col0" class="data row6 col0" >0.000000</td>
      <td id="T_a40eb_row6_col1" class="data row6 col1" >0.000000</td>
      <td id="T_a40eb_row6_col2" class="data row6 col2" >0.000000</td>
      <td id="T_a40eb_row6_col3" class="data row6 col3" >0.000000</td>
      <td id="T_a40eb_row6_col4" class="data row6 col4" >0.000000</td>
      <td id="T_a40eb_row6_col5" class="data row6 col5" >0.000000</td>
      <td id="T_a40eb_row6_col6" class="data row6 col6" >nan</td>
      <td id="T_a40eb_row6_col7" class="data row6 col7" >0.532454</td>
      <td id="T_a40eb_row6_col8" class="data row6 col8" >1.312500</td>
      <td id="T_a40eb_row6_col9" class="data row6 col9" >0.000000</td>
      <td id="T_a40eb_row6_col10" class="data row6 col10" >0.000000</td>
      <td id="T_a40eb_row6_col11" class="data row6 col11" >0.000000</td>
      <td id="T_a40eb_row6_col12" class="data row6 col12" >0.000000</td>
      <td id="T_a40eb_row6_col13" class="data row6 col13" >0.000000</td>
    </tr>
    <tr>
      <th id="T_a40eb_level0_row7" class="row_heading level0 row7" >Tower - Copper</th>
      <td id="T_a40eb_row7_col0" class="data row7 col0" >151.692308</td>
      <td id="T_a40eb_row7_col1" class="data row7 col1" >151.692308</td>
      <td id="T_a40eb_row7_col2" class="data row7 col2" >33.709402</td>
      <td id="T_a40eb_row7_col3" class="data row7 col3" >38.666667</td>
      <td id="T_a40eb_row7_col4" class="data row7 col4" >230.643275</td>
      <td id="T_a40eb_row7_col5" class="data row7 col5" >12.083333</td>
      <td id="T_a40eb_row7_col6" class="data row7 col6" >1.878095</td>
      <td id="T_a40eb_row7_col7" class="data row7 col7" >1.000000</td>
      <td id="T_a40eb_row7_col8" class="data row7 col8" >2.465000</td>
      <td id="T_a40eb_row7_col9" class="data row7 col9" >15.801282</td>
      <td id="T_a40eb_row7_col10" class="data row7 col10" >34.236111</td>
      <td id="T_a40eb_row7_col11" class="data row7 col11" >4.417563</td>
      <td id="T_a40eb_row7_col12" class="data row7 col12" >4.564815</td>
      <td id="T_a40eb_row7_col13" class="data row7 col13" >0.943089</td>
    </tr>
    <tr>
      <th id="T_a40eb_level0_row8" class="row_heading level0 row8" >Tower - Palisades</th>
      <td id="T_a40eb_row8_col0" class="data row8 col0" >61.538462</td>
      <td id="T_a40eb_row8_col1" class="data row8 col1" >61.538462</td>
      <td id="T_a40eb_row8_col2" class="data row8 col2" >13.675214</td>
      <td id="T_a40eb_row8_col3" class="data row8 col3" >15.686275</td>
      <td id="T_a40eb_row8_col4" class="data row8 col4" >93.567251</td>
      <td id="T_a40eb_row8_col5" class="data row8 col5" >4.901961</td>
      <td id="T_a40eb_row8_col6" class="data row8 col6" >0.761905</td>
      <td id="T_a40eb_row8_col7" class="data row8 col7" >0.405680</td>
      <td id="T_a40eb_row8_col8" class="data row8 col8" >1.000000</td>
      <td id="T_a40eb_row8_col9" class="data row8 col9" >6.410256</td>
      <td id="T_a40eb_row8_col10" class="data row8 col10" >13.888889</td>
      <td id="T_a40eb_row8_col11" class="data row8 col11" >1.792115</td>
      <td id="T_a40eb_row8_col12" class="data row8 col12" >1.851852</td>
      <td id="T_a40eb_row8_col13" class="data row8 col13" >0.382592</td>
    </tr>
    <tr>
      <th id="T_a40eb_level0_row9" class="row_heading level0 row9" >Galley - Copper</th>
      <td id="T_a40eb_row9_col0" class="data row9 col0" >4.800000</td>
      <td id="T_a40eb_row9_col1" class="data row9 col1" >4.800000</td>
      <td id="T_a40eb_row9_col2" class="data row9 col2" >1.600000</td>
      <td id="T_a40eb_row9_col3" class="data row9 col3" >2.447059</td>
      <td id="T_a40eb_row9_col4" class="data row9 col4" >3.649123</td>
      <td id="T_a40eb_row9_col5" class="data row9 col5" >0.764706</td>
      <td id="T_a40eb_row9_col6" class="data row9 col6" >inf</td>
      <td id="T_a40eb_row9_col7" class="data row9 col7" >0.063286</td>
      <td id="T_a40eb_row9_col8" class="data row9 col8" >0.156000</td>
      <td id="T_a40eb_row9_col9" class="data row9 col9" >1.000000</td>
      <td id="T_a40eb_row9_col10" class="data row9 col10" >0.433333</td>
      <td id="T_a40eb_row9_col11" class="data row9 col11" >0.849892</td>
      <td id="T_a40eb_row9_col12" class="data row9 col12" >0.072222</td>
      <td id="T_a40eb_row9_col13" class="data row9 col13" >0.014921</td>
    </tr>
    <tr>
      <th id="T_a40eb_level0_row10" class="row_heading level0 row10" >Frigate - Copper</th>
      <td id="T_a40eb_row10_col0" class="data row10 col0" >11.076923</td>
      <td id="T_a40eb_row10_col1" class="data row10 col1" >11.076923</td>
      <td id="T_a40eb_row10_col2" class="data row10 col2" >1.846154</td>
      <td id="T_a40eb_row10_col3" class="data row10 col3" >4.705882</td>
      <td id="T_a40eb_row10_col4" class="data row10 col4" >25.263158</td>
      <td id="T_a40eb_row10_col5" class="data row10 col5" >0.882353</td>
      <td id="T_a40eb_row10_col6" class="data row10 col6" >inf</td>
      <td id="T_a40eb_row10_col7" class="data row10 col7" >0.029209</td>
      <td id="T_a40eb_row10_col8" class="data row10 col8" >0.072000</td>
      <td id="T_a40eb_row10_col9" class="data row10 col9" >2.307692</td>
      <td id="T_a40eb_row10_col10" class="data row10 col10" >1.000000</td>
      <td id="T_a40eb_row10_col11" class="data row10 col11" >0.129032</td>
      <td id="T_a40eb_row10_col12" class="data row10 col12" >0.333333</td>
      <td id="T_a40eb_row10_col13" class="data row10 col13" >0.068867</td>
    </tr>
    <tr>
      <th id="T_a40eb_level0_row11" class="row_heading level0 row11" >Battleship - Copper</th>
      <td id="T_a40eb_row11_col0" class="data row11 col0" >64.384615</td>
      <td id="T_a40eb_row11_col1" class="data row11 col1" >64.384615</td>
      <td id="T_a40eb_row11_col2" class="data row11 col2" >14.307692</td>
      <td id="T_a40eb_row11_col3" class="data row11 col3" >36.470588</td>
      <td id="T_a40eb_row11_col4" class="data row11 col4" >97.894737</td>
      <td id="T_a40eb_row11_col5" class="data row11 col5" >6.838235</td>
      <td id="T_a40eb_row11_col6" class="data row11 col6" >inf</td>
      <td id="T_a40eb_row11_col7" class="data row11 col7" >0.226369</td>
      <td id="T_a40eb_row11_col8" class="data row11 col8" >0.558000</td>
      <td id="T_a40eb_row11_col9" class="data row11 col9" >1.176619</td>
      <td id="T_a40eb_row11_col10" class="data row11 col10" >7.750000</td>
      <td id="T_a40eb_row11_col11" class="data row11 col11" >1.000000</td>
      <td id="T_a40eb_row11_col12" class="data row11 col12" >2.583333</td>
      <td id="T_a40eb_row11_col13" class="data row11 col13" >0.533716</td>
    </tr>
    <tr>
      <th id="T_a40eb_level0_row12" class="row_heading level0 row12" >Sargon of Akkad</th>
      <td id="T_a40eb_row12_col0" class="data row12 col0" >33.230769</td>
      <td id="T_a40eb_row12_col1" class="data row12 col1" >33.230769</td>
      <td id="T_a40eb_row12_col2" class="data row12 col2" >8.181818</td>
      <td id="T_a40eb_row12_col3" class="data row12 col3" >9.773756</td>
      <td id="T_a40eb_row12_col4" class="data row12 col4" >14.860681</td>
      <td id="T_a40eb_row12_col5" class="data row12 col5" >3.000000</td>
      <td id="T_a40eb_row12_col6" class="data row12 col6" >inf</td>
      <td id="T_a40eb_row12_col7" class="data row12 col7" >0.219067</td>
      <td id="T_a40eb_row12_col8" class="data row12 col8" >0.540000</td>
      <td id="T_a40eb_row12_col9" class="data row12 col9" >13.846154</td>
      <td id="T_a40eb_row12_col10" class="data row12 col10" >3.000000</td>
      <td id="T_a40eb_row12_col11" class="data row12 col11" >0.387097</td>
      <td id="T_a40eb_row12_col12" class="data row12 col12" >1.000000</td>
      <td id="T_a40eb_row12_col13" class="data row12 col13" >0.206600</td>
    </tr>
    <tr>
      <th id="T_a40eb_level0_row13" class="row_heading level0 row13" >Gilgamesh</th>
      <td id="T_a40eb_row13_col0" class="data row13 col0" >160.846154</td>
      <td id="T_a40eb_row13_col1" class="data row13 col1" >160.846154</td>
      <td id="T_a40eb_row13_col2" class="data row13 col2" >39.602273</td>
      <td id="T_a40eb_row13_col3" class="data row13 col3" >47.307692</td>
      <td id="T_a40eb_row13_col4" class="data row13 col4" >71.929825</td>
      <td id="T_a40eb_row13_col5" class="data row13 col5" >14.520833</td>
      <td id="T_a40eb_row13_col6" class="data row13 col6" >inf</td>
      <td id="T_a40eb_row13_col7" class="data row13 col7" >1.060345</td>
      <td id="T_a40eb_row13_col8" class="data row13 col8" >2.613750</td>
      <td id="T_a40eb_row13_col9" class="data row13 col9" >67.019231</td>
      <td id="T_a40eb_row13_col10" class="data row13 col10" >14.520833</td>
      <td id="T_a40eb_row13_col11" class="data row13 col11" >1.873656</td>
      <td id="T_a40eb_row13_col12" class="data row13 col12" >4.840278</td>
      <td id="T_a40eb_row13_col13" class="data row13 col13" >1.000000</td>
    </tr>
  </tbody>
</table>
</div></div>


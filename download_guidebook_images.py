#!/usr/bin/env python3
"""Baixa do DokuWiki original (csr.ufmg.br) as imagens usadas pelas páginas de
docs/guidebook/ que ainda não estão em docs/image/.

Uso (a partir de qualquer pasta):
    python download_guidebook_images.py --dry-run     # só lista o que falta
    python download_guidebook_images.py               # baixa o que falta

Cada imagem é gravada em docs/image/ com o nome usado nas páginas; a tabela
IMAGENS abaixo relaciona esse nome ao id da mídia no DokuWiki. Imagens que já
existem são puladas, então o script pode ser executado de novo se for
interrompido. Só usa a biblioteca padrão (Python 3.8+).
"""
import argparse
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://csr.ufmg.br/dokuwiki/lib/exe/fetch.php"
USER_AGENT = "Mozilla/5.0 (dinamica-docs downloader)"

# nome local -> id da mídia no DokuWiki
IMAGENS = {
    "basic_overview_submodels.png": "submodels:basic_overview_submodels.png",
    "guidebook_15a.png": "15a.png",
    "guidebook_15b.png": "15b.png",
    "guidebook_15c.png": "15c.png",
    "guidebook_15d.png": "15d.png",
    "guidebook_15e.png": "15e.png",
    "guidebook_a.png": "a.png",
    "guidebook_a1.png": "a1.png",
    "guidebook_a10.png": "a10.png",
    "guidebook_a11.png": "a11.png",
    "guidebook_a12.png": "a12.png",
    "guidebook_a13.png": "a13.png",
    "guidebook_a2.png": "a2.png",
    "guidebook_a3.png": "a3.png",
    "guidebook_a4.png": "a4.png",
    "guidebook_a5.png": "a5.png",
    "guidebook_a6.png": "a6.png",
    "guidebook_a7.png": "a7.png",
    "guidebook_a8.png": "a8.png",
    "guidebook_a9.png": "a9.png",
    "guidebook_aaa10.png": "aaa10.png",
    "guidebook_aaa11.png": "aaa11.png",
    "guidebook_aaa2.png": "aaa2.png",
    "guidebook_aaa3.png": "aaa3.png",
    "guidebook_aaa5.png": "aaa5.png",
    "guidebook_aaa6.png": "aaa6.png",
    "guidebook_aaa7.png": "aaa7.png",
    "guidebook_aaa8.png": "aaa8.png",
    "guidebook_agent_based_model_agents_new2.jpg": "agent_based_model:agents_new2.jpg",
    "guidebook_agent_based_model_births_4.jpg": "agent_based_model:births_4.jpg",
    "guidebook_agent_based_model_coelhos4.jpg": "agent_based_model:coelhos4.jpg",
    "guidebook_agent_based_model_deaths_by_starvation3.jpg": "agent_based_model:deaths_by_starvation3.jpg",
    "guidebook_agent_based_model_gini_coefficient_new2.jpg": "agent_based_model:gini_coefficient_new2.jpg",
    "guidebook_agent_based_model_heterogeneos_landscape2.jpg": "agent_based_model:heterogeneos_landscape2.jpg",
    "guidebook_agent_based_model_heterogeneos_landscape_50_2.jpg": "agent_based_model:heterogeneos_landscape_50_2.jpg",
    "guidebook_agent_based_model_homogeneos_landscape2.jpg": "agent_based_model:homogeneos_landscape2.jpg",
    "guidebook_agent_based_model_mils.jpg": "agent_based_model:mils.jpg",
    "guidebook_agent_based_model_movement_intake_and_recovery.jpg": "agent_based_model:movement_intake_and_recovery.jpg",
    "guidebook_agent_based_model_pop_landscape4.jpg": "agent_based_model:pop_landscape4.jpg",
    "guidebook_agent_based_model_resources2.jpg": "agent_based_model:resources2.jpg",
    "guidebook_agent_based_model_rules.jpg": "agent_based_model:rules.jpg",
    "guidebook_agent_based_model_types_new_2.jpg": "agent_based_model:types_new_2.jpg",
    "guidebook_agent_based_model_typing_2.jpg": "agent_based_model:typing_2.jpg",
    "guidebook_agent_based_model_vensim2.jpg": "agent_based_model:vensim2.jpg",
    "guidebook_b.png": "b.png",
    "guidebook_b1.png": "b1.png",
    "guidebook_b2.png": "b2.png",
    "guidebook_b3.png": "b3.png",
    "guidebook_b4.png": "b4.png",
    "guidebook_b5.png": "b5.png",
    "guidebook_b6.png": "b6.png",
    "guidebook_b7.png": "b7.png",
    "guidebook_c1.png": "c1.png",
    "guidebook_c10.png": "c10.png",
    "guidebook_c11.png": "c11.png",
    "guidebook_c12.png": "c12.png",
    "guidebook_c13.png": "c13.png",
    "guidebook_c14.png": "c14.png",
    "guidebook_c2.png": "c2.png",
    "guidebook_c3.png": "c3.png",
    "guidebook_c4.png": "c4.png",
    "guidebook_c5.png": "c5.png",
    "guidebook_c6.png": "c6.png",
    "guidebook_c7.png": "c7.png",
    "guidebook_c8.png": "c8.png",
    "guidebook_c9.png": "c9.png",
    "guidebook_cost1.1.jpg": "tutorial:cost1.1.jpg",
    "guidebook_cost10.jpg": "tutorial:cost10.jpg",
    "guidebook_cost11.2.jpg": "tutorial:cost11.2.jpg",
    "guidebook_cost12.jpg": "tutorial:cost12.jpg",
    "guidebook_cost13.2.jpg": "tutorial:cost13.2.jpg",
    "guidebook_cost2.jpg": "tutorial:cost2.jpg",
    "guidebook_cost3.jpg": "tutorial:cost3.jpg",
    "guidebook_cost4.jpg": "tutorial:cost4.jpg",
    "guidebook_cost5.jpg": "tutorial:cost5.jpg",
    "guidebook_cost6.1.jpg": "tutorial:cost6.1.jpg",
    "guidebook_cost8.2.jpg": "tutorial:cost8.2.jpg",
    "guidebook_cost9.jpg": "tutorial:cost9.jpg",
    "guidebook_d1.png": "d1.png",
    "guidebook_d10.png": "d10.png",
    "guidebook_d11.png": "d11.png",
    "guidebook_d12.png": "d12.png",
    "guidebook_d13.png": "d13.png",
    "guidebook_d14.png": "d14.png",
    "guidebook_d15.png": "d15.png",
    "guidebook_d16.png": "d16.png",
    "guidebook_d18.png": "d18.png",
    "guidebook_d2.png": "d2.png",
    "guidebook_d3.png": "d3.png",
    "guidebook_d4.png": "d4.png",
    "guidebook_d5.png": "d5.png",
    "guidebook_d6.png": "d6.png",
    "guidebook_d7.png": "d7.png",
    "guidebook_d8.png": "d8.png",
    "guidebook_d9.png": "d9.png",
    "guidebook_data_cell_types.jpg": "tutorial:data_cell_types.jpg",
    "guidebook_ga_1.1.jpg": "tutorial:ga_1.1.jpg",
    "guidebook_ga_2.jpg": "tutorial:ga_2.jpg",
    "guidebook_ga_3.jpg": "tutorial:ga_3.jpg",
    "guidebook_ga__4.jpg": "tutorial:ga_ 4.jpg",
    "guidebook_ga__5.1.jpg": "tutorial:ga_ 5.1.jpg",
    "guidebook_imagem000.png": "imagem000.png",
    "guidebook_imagem11.png": "imagem11.png",
    "guidebook_imagem12.png": "imagem12.png",
    "guidebook_imagem13.png": "imagem13.png",
    "guidebook_imagem15.png": "imagem15.png",
    "guidebook_imagem16.png": "imagem16.png",
    "guidebook_imagem17.png": "imagem17.png",
    "guidebook_imagem18.png": "imagem18.png",
    "guidebook_imagem19.png": "imagem19.png",
    "guidebook_imagem20.png": "imagem20.png",
    "guidebook_imagem21.png": "imagem21.png",
    "guidebook_imagem22.png": "imagem22.png",
    "guidebook_imagem23.png": "imagem23.png",
    "guidebook_imagem24.png": "imagem24.png",
    "guidebook_imagem25.png": "imagem25.png",
    "guidebook_imagem26.png": "imagem26.png",
    "guidebook_imagem27.png": "imagem27.png",
    "guidebook_imagem28.png": "imagem28.png",
    "guidebook_imagem29.png": "imagem29.png",
    "guidebook_imagem31.png": "imagem31.png",
    "guidebook_imagem32.png": "imagem32.png",
    "guidebook_imagem33.png": "imagem33.png",
    "guidebook_imagem34.png": "imagem34.png",
    "guidebook_imagem35.png": "imagem35.png",
    "guidebook_imagem36.png": "imagem36.png",
    "guidebook_imagem37.png": "imagem37.png",
    "guidebook_imagem38.png": "imagem38.png",
    "guidebook_imagem39.png": "imagem39.png",
    "guidebook_imagem40.png": "imagem40.png",
    "guidebook_imagem41.png": "imagem41.png",
    "guidebook_imagem42.png": "imagem42.png",
    "guidebook_imagem43.png": "imagem43.png",
    "guidebook_imagem44.png": "imagem44.png",
    "guidebook_imagem45.png": "imagem45.png",
    "guidebook_imagem46.png": "imagem46.png",
    "guidebook_imagem47.png": "imagem47.png",
    "guidebook_imagem48.png": "imagem48.png",
    "guidebook_imagem49.png": "imagem49.png",
    "guidebook_imagem50.png": "imagem50.png",
    "guidebook_imagem51.png": "imagem51.png",
    "guidebook_imagem53.png": "imagem53.png",
    "guidebook_imagem67.png": "imagem67.png",
    "guidebook_imagem68.png": "imagem68.png",
    "guidebook_imagem69.png": "imagem69.png",
    "guidebook_imagem7.png": "imagem7.png",
    "guidebook_imagem70.png": "imagem70.png",
    "guidebook_imagem71.png": "imagem71.png",
    "guidebook_imagem72.png": "imagem72.png",
    "guidebook_imagem73.png": "imagem73.png",
    "guidebook_imagem74.png": "imagem74.png",
    "guidebook_imagem75.png": "imagem75.png",
    "guidebook_imagem76.png": "imagem76.png",
    "guidebook_imagem77.png": "imagem77.png",
    "guidebook_imagem78.png": "imagem78.png",
    "guidebook_imagem79.png": "imagem79.png",
    "guidebook_imagem8.png": "imagem8.png",
    "guidebook_imagem80.png": "imagem80.png",
    "guidebook_imagem81.png": "imagem81.png",
    "guidebook_imagem82.jpg": "imagem82.jpg",
    "guidebook_imagem86.png": "imagem86.png",
    "guidebook_images_habitatmod_figure03.png": "images:habitatmod_figure03.png",
    "guidebook_inc._it._model_17.jpg": "tutorial:inc._it._model_17.jpg",
    "guidebook_landscape_1.jpg": "tutorial:landscape_1.jpg",
    "guidebook_logo_guidebook1.jpg": "logo_guidebook1.jpg",
    "guidebook_lucc_10.jpg": "tutorial:lucc_10.jpg",
    "guidebook_lucc_11.jpg": "tutorial:lucc_11.jpg",
    "guidebook_lucc_12.3.jpg": "tutorial:lucc_12.3.jpg",
    "guidebook_lucc_13.jpg": "tutorial:lucc_13.jpg",
    "guidebook_lucc_14.jpg": "tutorial:lucc_14.jpg",
    "guidebook_lucc_16.jpg": "tutorial:lucc_16.jpg",
    "guidebook_lucc_17.1.jpg": "tutorial:lucc_17.1.jpg",
    "guidebook_lucc_18.jpg": "tutorial:lucc_18.jpg",
    "guidebook_lucc_19.jpg": "tutorial:lucc_19.jpg",
    "guidebook_lucc_2.jpg": "tutorial:lucc_2.jpg",
    "guidebook_lucc_20.jpg": "tutorial:lucc_20.jpg",
    "guidebook_lucc_21.jpg": "tutorial:lucc_21.jpg",
    "guidebook_lucc_22.1.jpg": "tutorial:lucc_22.1.jpg",
    "guidebook_lucc_23.1.jpg": "tutorial:lucc_23.1.jpg",
    "guidebook_lucc_25.jpg": "tutorial:lucc_25.jpg",
    "guidebook_lucc_26.2.jpg": "tutorial:lucc_26.2.jpg",
    "guidebook_lucc_26.3.jpg": "tutorial:lucc_26.3.jpg",
    "guidebook_lucc_27.2.jpg": "tutorial:lucc_27.2.jpg",
    "guidebook_lucc_28.jpg": "tutorial:lucc_28.jpg",
    "guidebook_lucc_29.jpg": "tutorial:lucc_29.jpg",
    "guidebook_lucc_3.jpg": "tutorial:lucc_3.jpg",
    "guidebook_lucc_30.jpg": "tutorial:lucc_30.jpg",
    "guidebook_lucc_31.jpg": "tutorial:lucc_31.jpg",
    "guidebook_lucc_32.2.jpg": "tutorial:lucc_32.2.jpg",
    "guidebook_lucc_33.5.jpg": "tutorial:lucc_33.5.jpg",
    "guidebook_lucc_34.2.jpg": "tutorial:lucc_34.2.jpg",
    "guidebook_lucc_35.2.jpg": "tutorial:lucc_35.2.jpg",
    "guidebook_lucc_36.6.jpg": "tutorial:lucc_36.6.jpg",
    "guidebook_lucc_36.jpg": "tutorial:lucc_36.jpg",
    "guidebook_lucc_38.1.jpg": "tutorial:lucc_38.1.jpg",
    "guidebook_lucc_39.jpg": "tutorial:lucc_39.jpg",
    "guidebook_lucc_4.jpg": "tutorial:lucc_4.jpg",
    "guidebook_lucc_40.1.jpg": "tutorial:lucc_40.1.jpg",
    "guidebook_lucc_40.jpg": "tutorial:lucc_40.jpg",
    "guidebook_lucc_41.2.jpg": "tutorial:lucc_41.2.jpg",
    "guidebook_lucc_42.jpg": "tutorial:lucc_42.jpg",
    "guidebook_lucc_43.3.jpg": "tutorial:lucc_43.3.jpg",
    "guidebook_lucc_44.jpg": "tutorial:lucc_44.jpg",
    "guidebook_lucc_48.1.jpg": "tutorial:lucc_48.1.jpg",
    "guidebook_lucc_49.jpg": "tutorial:lucc_49.jpg",
    "guidebook_lucc_5.jpg": "tutorial:lucc_5.jpg",
    "guidebook_lucc_50.1.jpg": "tutorial:lucc_50.1.jpg",
    "guidebook_lucc_56.jpg": "tutorial:lucc_56.jpg",
    "guidebook_lucc_57.jpg": "tutorial:lucc_57.jpg",
    "guidebook_lucc_6.jpg": "tutorial:lucc_6.jpg",
    "guidebook_lucc_60.1.jpg": "tutorial:lucc_60.1.jpg",
    "guidebook_lucc_61.2.jpg": "tutorial:lucc_61.2.jpg",
    "guidebook_lucc_62.1.jpg": "tutorial:lucc_62.1.jpg",
    "guidebook_lucc_63.1.jpg": "tutorial:lucc_63.1.jpg",
    "guidebook_lucc_64.jpg": "tutorial:lucc_64.jpg",
    "guidebook_lucc_65.jpg": "tutorial:lucc_65.jpg",
    "guidebook_lucc_66.jpg": "tutorial:lucc_66.jpg",
    "guidebook_lucc_67.jpg": "tutorial:lucc_67.jpg",
    "guidebook_lucc_68.jpg": "tutorial:lucc_68.jpg",
    "guidebook_lucc_69.1.jpg": "tutorial:lucc_69.1.jpg",
    "guidebook_lucc_7.jpg": "tutorial:lucc_7.jpg",
    "guidebook_lucc_8.1.jpg": "tutorial:lucc_8.1.jpg",
    "guidebook_lucc_8.2.jpg": "tutorial:lucc_8.2.jpg",
    "guidebook_lucc_9.jpg": "tutorial:lucc_9.jpg",
    "guidebook_mce10.jpg": "tutorial:mce10.jpg",
    "guidebook_mce11.jpg": "tutorial:mce11.jpg",
    "guidebook_mce12.jpg": "tutorial:mce12.jpg",
    "guidebook_mce13.jpg": "tutorial:mce13.jpg",
    "guidebook_mce14.jpg": "tutorial:mce14.jpg",
    "guidebook_mce15.jpg": "tutorial:mce15.jpg",
    "guidebook_mce16.jpg": "tutorial:mce16.jpg",
    "guidebook_mce18.jpg": "tutorial:mce18.jpg",
    "guidebook_mce19.jpg": "tutorial:mce19.jpg",
    "guidebook_mce21.jpg": "tutorial:mce21.jpg",
    "guidebook_mce22.jpg": "tutorial:mce22.jpg",
    "guidebook_mce23.jpg": "tutorial:mce23.jpg",
    "guidebook_mce24.jpg": "tutorial:mce24.jpg",
    "guidebook_mce25.jpg": "tutorial:mce25.jpg",
    "guidebook_mce26.jpg": "tutorial:mce26.jpg",
    "guidebook_mce27.jpg": "tutorial:mce27.jpg",
    "guidebook_mce28.jpg": "tutorial:mce28.jpg",
    "guidebook_mce29.jpg": "tutorial:mce29.jpg",
    "guidebook_mce3.jpg": "tutorial:mce3.jpg",
    "guidebook_mce30.jpg": "tutorial:mce30.jpg",
    "guidebook_mce31.jpg": "tutorial:mce31.jpg",
    "guidebook_mce32.jpg": "tutorial:mce32.jpg",
    "guidebook_mce33.jpg": "tutorial:mce33.jpg",
    "guidebook_mce4.jpg": "tutorial:mce4.jpg",
    "guidebook_mce5.jpg": "tutorial:mce5.jpg",
    "guidebook_mce6.jpg": "tutorial:mce6.jpg",
    "guidebook_mce7.2.jpg": "tutorial:mce7.2.jpg",
    "guidebook_mce8.jpg": "tutorial:mce8.jpg",
    "guidebook_mce9.jpg": "tutorial:mce9.jpg",
    "guidebook_mce_1.2.jpg": "tutorial:mce_1.2.jpg",
    "guidebook_mce_2.jpg": "tutorial:mce_2.jpg",
    "guidebook_model3.jpg": "model3.jpg",
    "guidebook_patterns_2.png": "patterns_2.png",
    "guidebook_patterns_3.png": "patterns_3.png",
    "guidebook_patterns_4.png": "patterns_4.png",
    "guidebook_patterns_5.png": "patterns_5.png",
    "guidebook_patterns_6.png": "patterns_6.png",
    "guidebook_pratical_application.png": "pratical_application.png",
    "guidebook_rc1.png": "rc1.png",
    "guidebook_rc2.png": "rc2.png",
    "guidebook_redd_1.jpg": "tutorial:redd_1.jpg",
    "guidebook_redd_10.1.jpg": "tutorial:redd_10.1.jpg",
    "guidebook_redd_11.jpg": "tutorial:redd_11.jpg",
    "guidebook_redd_12.jpg": "tutorial:redd_12.jpg",
    "guidebook_redd_2.jpg": "tutorial:redd_2.jpg",
    "guidebook_redd_3.jpg": "tutorial:redd_3.jpg",
    "guidebook_redd_4.jpg": "tutorial:redd_4.jpg",
    "guidebook_redd_5.jpg": "tutorial:redd_5.jpg",
    "guidebook_redd_6.jpg": "tutorial:redd_6.jpg",
    "guidebook_redd_7.jpg": "tutorial:redd_7.jpg",
    "guidebook_redd_8.1.jpg": "tutorial:redd_8.1.jpg",
    "guidebook_redd_9.jpg": "tutorial:redd_9.jpg",
    "guidebook_region1.jpg": "tutorial:region1.jpg",
    "guidebook_region2.jpg": "tutorial:region2.jpg",
    "guidebook_region3.jpg": "tutorial:region3.jpg",
    "guidebook_region5.jpg": "tutorial:region5.jpg",
    "guidebook_region6.jpg": "tutorial:region6.jpg",
    "guidebook_region7.jpg": "tutorial:region7.jpg",
    "guidebook_script_1.1.jpg": "tutorial:script_1.1.jpg",
    "guidebook_script_2.1.jpg": "tutorial:script_2.1.jpg",
    "guidebook_script_3.1.jpg": "tutorial:script_3.1.jpg",
    "guidebook_script_4.1.jpg": "tutorial:script_4.1.jpg",
    "guidebook_steps_lucc_model.png": "steps_lucc_model.png",
    "guidebook_wizard_add_input.png": "wizard:add_input.png",
    "guidebook_wizard_create_page.png": "wizard:create_page.png",
    "guidebook_wizard_create_page2.png": "wizard:create_page2.png",
    "guidebook_wizard_edit_wizard.png": "wizard:edit_wizard.png",
    "guidebook_wizard_editor1.png": "wizard:editor1.png",
    "guidebook_wizard_editor2.png": "wizard:editor2.png",
    "guidebook_wizard_editor3.png": "wizard:editor3.png",
    "guidebook_wizard_editor_interface.png": "wizard:editor_interface.png",
    "guidebook_wizard_editor_menu.png": "wizard:editor_menu.png",
    "guidebook_wizard_expression.png": "wizard:expression.png",
    "guidebook_wizard_functor_selector.png": "wizard:functor_selector.png",
    "guidebook_wizard_input_description.png": "wizard:input_description.png",
    "guidebook_wizard_input_description_edited.png": "wizard:input_description_edited.png",
    "guidebook_wizard_model.png": "wizard:model.png",
    "guidebook_wizard_next_step.png": "wizard:next_step.png",
    "guidebook_wizard_output_description.png": "wizard:output_description.png",
    "guidebook_wizard_page_editor1.png": "wizard:page_editor1.png",
    "guidebook_wizard_page_input_buttons.png": "wizard:page_input_buttons.png",
    "guidebook_wizard_page_inputs_new.png": "wizard:page_inputs_new.png",
    "guidebook_wizard_page_name.png": "wizard:page_name.png",
    "guidebook_wizard_page_text1.png": "wizard:page_text1.png",
    "guidebook_wizard_page_text_formatted.png": "wizard:page_text_formatted.png",
    "guidebook_wizard_run_model.png": "wizard:run_model.png",
    "guidebook_wizard_run_wizard_button_toolbar.png": "wizard:run_wizard_button_toolbar.png",
    "guidebook_wizard_run_wizard_prompt.png": "wizard:run_wizard_prompt.png",
    "guidebook_wizard_save.png": "wizard:save.png",
    "guidebook_wizard_test_wizard_button.png": "wizard:test_wizard_button.png",
    "guidebook_wizard_third_page_created.png": "wizard:third_page_created.png",
    "guidebook_wizard_third_page_edit.png": "wizard:third_page_edit.png",
    "guidebook_wizard_third_page_inputs.png": "wizard:third_page_inputs.png",
    "guidebook_wizard_wizard_model_correspondence.png": "wizard:wizard_model_correspondence.png",
    "guidebook_wizard_wizard_presentation.png": "wizard:wizard_presentation.png",
    "guidebook_wizard_wizr_editor.png": "wizard:wizr_editor.png",
    "localbadge16.png": "submodels:localbadge16.png",
    "map_viewer_apply_map_alias.png": "map_viewer:apply_map_alias.png",
    "map_viewer_change_alias.gif": "map_viewer:change_alias.gif",
    "map_viewer_histogram.png": "map_viewer:histogram.png",
    "map_viewer_loaded_map_buttons.png": "map_viewer:loaded_map_buttons.png",
    "map_viewer_main_window.jpg": "map_viewer:map_viewer.jpg",
    "map_viewer_map_alias_showing.png": "map_viewer:map_alias_showing.png",
    "map_viewer_map_info.png": "map_viewer:map_info.png",
    "map_viewer_map_information_icon.png": "map_viewer:map_information_icon.png",
    "map_viewer_palette.png": "map_viewer:palette.png",
    "map_viewer_palette_color_hover.png": "map_viewer:palette_color_hover.png",
    "map_viewer_palette_gradient.png": "map_viewer:palette_gradient.png",
    "map_viewer_restore_original_alias.png": "map_viewer:restore_original_alias.png",
    "map_viewer_toolbar.png": "map_viewer:toolbar_num.png",
    "movie_1.png": "movie:movie_1.png",
    "movie_2.png": "movie:movie_2.png",
    "movie_3.png": "movie:movie_3.png",
    "movie_4.png": "movie:movie_4.png",
    "movie_5.png": "movie:movie_5.png",
    "movie_maker_button.png": "movie:movie_maker_button.png",
    "submodel_functor_library.png": "submodels:submodel_functor_library.png",
    "submodel_types.png": "submodels:submodel_types.png",
    "submodel_with_badge.png": "submodels:submodel_with_badge.png",
    "systembadge16.png": "submodels:systembadge16.png",
    "userbadge16.png": "submodels:userbadge16.png",
}

MAGIC = (b"\x89PNG", b"\xff\xd8\xff", b"GIF8")


def buscar(url, tentativas=3, timeout=60):
    erro = None
    for i in range(tentativas):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (401, 403, 404):
                raise
            erro = e
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            erro = e
        time.sleep(2 * (i + 1))
    raise erro


def main():
    raiz = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="só lista as imagens que faltam")
    ap.add_argument("--delay", type=float, default=0.5, help="pausa entre requisições, em segundos")
    ap.add_argument("--dest", type=Path, default=raiz / "docs" / "image", help="pasta de destino")
    ap.add_argument("--base", default=BASE, help="URL do fetch.php")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

    args.dest.mkdir(parents=True, exist_ok=True)
    faltam = {n: i for n, i in IMAGENS.items() if not (args.dest / n).exists()}
    print(f"Imagens listadas: {len(IMAGENS)} | já presentes: {len(IMAGENS) - len(faltam)} | faltando: {len(faltam)}")
    if args.dry_run:
        for nome, id_midia in faltam.items():
            print(f"   {nome:<45} <- {id_midia}")
        return 0

    contagem = {"ok": 0, "failed": 0}
    log = raiz / "download_log_images.txt"
    with log.open("a", encoding="utf-8", newline="\n") as f:
        for n, (nome, id_midia) in enumerate(faltam.items(), 1):
            url = f"{args.base}?media={urllib.parse.quote(id_midia, safe=':')}"
            try:
                dados = buscar(url)
                if not dados.startswith(MAGIC):
                    raise ValueError("a resposta não é uma imagem (página de erro ou de login?)")
                (args.dest / nome).write_bytes(dados)
                estado = "ok"
            except Exception as e:
                estado = "failed"
                print(f"  erro em {nome}: {e}")
            contagem[estado] += 1
            f.write(f"[{estado}]".ljust(10) + f" {nome:<45} {url}\n")
            f.flush()
            print(f"[{n}/{len(faltam)}] {estado:6} {nome}")
            time.sleep(args.delay)
    print(f"Concluído: {contagem['ok']} baixadas, {contagem['failed']} com falha.")
    print(f"Log: {log}")
    return 1 if contagem["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())

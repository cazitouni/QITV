import xml.etree.ElementTree as ET

from .mapper import (
    caracterisation_1,
    caracterisation_2,
    etape_inspection,
    format_image,
    format_video,
    forme,
    materiau,
    methode_inspection,
    nettoyage,
    objet_inspection,
    observation,
    point_depart_lateral,
    point_reference_longitudinal,
    position_bande_video,
    precipitations,
    propriete_fonciere,
    regulation_debit,
    sens_ecoulement,
    support_media,
    temperature,
    type_branchement,
    type_emplacement,
    type_revetement,
    utilisation_branchement,
)


def get_text_safe(element, tag):
    """Safely extract text from XML element"""
    child = element.find(tag)
    return child.text if child is not None and child.text is not None else ""


def resolve_characterisation(code_principal, field_code, mapping_dict):
    if code_principal in mapping_dict:
        return mapping_dict[code_principal].get(
            field_code, f"Code principal inconnu : '{field_code}'"
        )
    else:
        return None


def itv_parser(xml_data):
    tree = ET.parse(xml_data)
    root = tree.getroot()
    segments = []
    for zb in root.findall("ZB"):
        numero_troncon = get_text_safe(zb, "AAA")
        # Retourne le numéro en cas de besoin si le sens de controle est
        # opposé au sens de la cana
        if get_text_safe(zb, "AAK") == "B" and "-" in numero_troncon:
            parts = numero_troncon.split("-")
            if len(parts) == 2:
                numero_troncon = f"{parts[1]}-{parts[0]}"
        ###########################################################################################
        segment_data = {
            "numero_troncon": numero_troncon,
            "id_noeud_depart": get_text_safe(zb, "AAB"),
            "coord_noeud_depart": get_text_safe(zb, "AAC"),
            "id_noeud_1": get_text_safe(zb, "AAD"),
            "coord_noeud_1": get_text_safe(zb, "AAE"),
            "id_noeud_2": get_text_safe(zb, "AAF"),
            "coord_noeud_2": get_text_safe(zb, "AAG"),
            "depart_longitudinal_troncon": get_text_safe(zb, "AAH"),
            "depart_circonferentiel_troncon": get_text_safe(zb, "AAI"),
            "emplacement": get_text_safe(zb, "AAJ"),
            "sens_ecoulement": sens_ecoulement.get(
                get_text_safe(zb, "AAK"), get_text_safe(zb, "AAK")
            ),
            "type_emplacement": type_emplacement.get(
                get_text_safe(zb, "AAL"), get_text_safe(zb, "AAL")
            ),
            "responsable": get_text_safe(zb, "AAM"),
            "comunne": get_text_safe(zb, "AAN"),
            "quartier": get_text_safe(zb, "AAO"),
            "nom_reseau": get_text_safe(zb, "AAP"),
            "propriete_fonciere": propriete_fonciere.get(
                get_text_safe(zb, "AAQ"), get_text_safe(zb, "AAQ")
            ),
            "id_noeud_3": get_text_safe(zb, "AAT"),
            "coord_noeud_3": get_text_safe(zb, "AAU"),
            "point_depart_lateral": point_depart_lateral.get(
                get_text_safe(zb, "AAV"), get_text_safe(zb, "AAV")
            ),
            "norme": get_text_safe(zb, "ABA"),
            "systeme_codage": get_text_safe(zb, "ABB"),
            "point_reference_longitudinal": point_reference_longitudinal.get(
                get_text_safe(zb, "ABC"), get_text_safe(zb, "ABC")
            ),
            "methode_inspection": methode_inspection.get(
                get_text_safe(zb, "ABE"), get_text_safe(zb, "ABE")
            ),
            "date_inspection": get_text_safe(zb, "ABF"),
            "heure_inspection": get_text_safe(zb, "ABG"),
            "inspecteur": get_text_safe(zb, "ABH"),
            "ref_fonction_inspecteur": get_text_safe(zb, "ABI"),
            "ref_fonction_employeur": get_text_safe(zb, "ABJ"),
            "support_media": support_media.get(
                get_text_safe(zb, "ABK"), get_text_safe(zb, "ABK")
            ),
            "format_image": format_image.get(
                get_text_safe(zb, "ABL"), get_text_safe(zb, "ABL")
            ),
            "position_bande_video": position_bande_video.get(
                get_text_safe(zb, "ABM"), get_text_safe(zb, "ABM")
            ),
            "ref_photo": get_text_safe(zb, "ABN"),
            "ref_video": get_text_safe(zb, "ABO"),
            "objet_inspection": objet_inspection.get(
                get_text_safe(zb, "ABP"), get_text_safe(zb, "ABP")
            ),
            "etendue_inspection_prevue": float(get_text_safe(zb, "ABQ")),
            "format_video": format_video.get(
                get_text_safe(zb, "ABR"), get_text_safe(zb, "ABR")
            ),
            "nom_video": get_text_safe(zb, "ABS"),
            "etape_inspection": etape_inspection.get(
                get_text_safe(zb, "ABT"), get_text_safe(zb, "ABT")
            ),
            "forme": forme.get(get_text_safe(zb, "ACA"), get_text_safe(zb, "ACA")),
            "hauteur": get_text_safe(zb, "ACB"),
            "largeur": get_text_safe(zb, "ACC"),
            "materiau": materiau.get(
                get_text_safe(zb, "ACD"), get_text_safe(zb, "ACD")
            ),
            "type_revetement": type_revetement.get(
                get_text_safe(zb, "ACE"), get_text_safe(zb, "ACE")
            ),
            "materiau_revetement": materiau.get(
                get_text_safe(zb, "ACF"), get_text_safe(zb, "ACF")
            ),
            "longueur_unitaire": get_text_safe(zb, "ACG"),
            "profondeur_noeud_depart": get_text_safe(zb, "ACH"),
            "profondeur_noeud_arrivee": get_text_safe(zb, "ACI"),
            "type_branchement": type_branchement.get(
                get_text_safe(zb, "ACJ"), get_text_safe(zb, "ACJ")
            ),
            "utilisation_branchement": utilisation_branchement.get(
                get_text_safe(zb, "ACK"), get_text_safe(zb, "ACK")
            ),
            "position_strategique": get_text_safe(zb, "ACL"),
            "nettoyage": nettoyage.get(
                get_text_safe(zb, "ACM"), get_text_safe(zb, "ACM")
            ),
            "annee_mise_service": get_text_safe(zb, "ACN"),
            "precipitations": precipitations.get(
                get_text_safe(zb, "ADA"), get_text_safe(zb, "ADA")
            ),
            "temperature": temperature.get(
                get_text_safe(zb, "ADB"), get_text_safe(zb, "ADB")
            ),
            "regulation_debit": regulation_debit.get(
                get_text_safe(zb, "ADC"), get_text_safe(zb, "ADC")
            ),
            "remarque_generale": get_text_safe(zb, "ADE"),
        }
        zc_list = []
        for zc in zb.findall("ZC"):
            zc_data = {
                "observation": observation.get(
                    get_text_safe(zc, "A"), get_text_safe(zc, "A")
                ),
                "caracterisation_1": resolve_characterisation(
                    get_text_safe(zc, "A"), get_text_safe(zc, "B"), caracterisation_1
                ),
                "caracterisation_2": resolve_characterisation(
                    get_text_safe(zc, "A"), get_text_safe(zc, "C"), caracterisation_2
                ),
                "quantification_1": get_text_safe(zc, "D"),
                "quantification_2": get_text_safe(zc, "E"),
                "remarques": get_text_safe(zc, "F"),
                "emplacement_circonf_1": get_text_safe(zc, "G"),
                "emplacement_circonf_2": get_text_safe(zc, "H"),
                "emplacement_longitudinal": get_text_safe(zc, "I"),
                "code_defaut_continu": get_text_safe(zc, "J"),
                "assemblage": get_text_safe(zc, "K"),
                "champ_description_emplacement": get_text_safe(zc, "L"),
                "ref_photo": get_text_safe(zc, "M"),
                "ref_video": get_text_safe(zc, "N"),
            }
            zc_list.append(zc_data)
        segment_data["observation"] = zc_list
        segments.append(segment_data)

    return segments

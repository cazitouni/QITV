sens_ecoulement = {
    "A": "aval — inspection réalisée dans le même sens que l'écoulement normal",
    "B": "amont — inspection réalisée dans le sens opposé à l'écoulement normal",
    "C": "inconnu — le sens normal d'écoulement est inconnu",
}

type_emplacement = {
    "A": "Sous une route",
    "B": "Sous un trottoir",
    "C": "Sous l'accotement d'une route",
    "D": "Dans une autre zone piétonnière",
    "E": "Dans un champ",
    "F": "Sous une propriété bâtie",
    "G": "Sous des jardins",
    "H": "Sous un bâtiment permanent",
    "I": "Sous un terrain boisé",
    "J": "Accès difficile (ex : autoroute ou voie ferrée en service)",
    "K": "Sous une voie navigable",
    "Z": "Autre (voir remarque ADE)",
}

propriete_fonciere = {"A": "bien public", "B": "bien privé", "C": "inconnue"}

point_depart_lateral = {
    "A": "raccordement au collecteur principal",
    "B": "troisième noeud",
}

point_reference_longitudinal = {
    "A": "Face intérieure de la paroi du noeud de départ (regard de visite, boîte d’inspection, déversoir, etc.) au point de raccordement",
    "B": "Intrados du tronçon à l'intérieur du noeud de départ",
    "C": "Centre du regard de visite ou de la boîte d’inspection de départ",
    "D": "Point central des canalisations entrantes et sortantes, mesuré le long de la cunette",
    "Z": "Autre (spécifié à l'aide d'un code de remarque générale ADE)",
}

methode_inspection = {
    "A": "Inspection directe du branchement ou du collecteur par un inspecteur se déplaçant dans la canalisation",
    "B": "Inspection par une télécaméra circulant dans la canalisation",
    "C": "Inspection à partir du regard de visite ou de la boîte d’inspection uniquement",
}

support_media = {
    "A": "Cassette vidéo VHS",
    "B": "CD vidéo",
    "C": "DVD vidéo",
    "D": "CD de données",
    "E": "DVD de données",
    "F": "Disque dur portable",
    "Z": "Autre (avec code de remarque générale ADE)",
}

format_image = {
    "A": "Images fixes",
    "B": "Hors d'usage — données existantes devant s'énoncer comme si la caractérisation était Z",
    "C": "Windows Meta File — WMF",
    "D": "Graphic Image File — GIF",
    "E": "JPEG",
    "Z": "Autre (avec code de remarque générale ADE)",
}

position_bande_video = {
    "A": "Durée d'enregistrement en heures et en minutes depuis le début de la bande",
    "B": "Compteur numérique dépendant de la machine",
    "Z": "Autre (avec code de remarque générale ADE)",
}

objet_inspection = {
    "A": "Contrôle final d’une nouvelle construction",
    "B": "Fin de la période de garantie",
    "C": "Inspection de routine de l’état",
    "D": "Problème structurel suspecté",
    "E": "Problème opérationnel suspecté",
    "F": "Problème d’infiltration suspecté",
    "G": "Contrôle final de travaux de rénovation ou de réparation",
    "H": "Transfert de propriété",
    "I": "Planification d’investissement",
    "J": "Étude par échantillon",
    "Z": "Autre (avec code de remarque générale ADE)",
}

format_video = {
    "A": "Type fixe sur support (par exemple, les formats de bande vidéo)",
    "B": "MPEG1",
    "C": "MPEG2",
    "D": "MPEG4",
    "Z": "Autre (avec code de remarque générale ADE)",
}

etape_inspection = {
    "A": "De l'autorité responsable à l'inspecteur",
    "B": "De l'inspecteur à l'autorité responsable pour étude",
    "C": "Dans les mains de l'autorité responsable après étude",
    "Z": "Autre (avec code de remarque générale ADE)",
}

forme = {
    "A": "Circulaire",
    "B": "Rectangulaire",
    "C": "Ovoïde",
    "D": "En U — radier demi-circulaire, dessus plat et pieds droits parallèles",
    "E": "En arc — voûte demi-circulaire, radier plat et pieds droits parallèles",
    "F": "Ovale — radier et voûte demi-circulaires (de même diamètre) et pieds droits parallèles",
    "Z": "Autre (avec code de remarque générale ADE)",
}

materiau = {
    "AA": "Amiante-ciment",
    "AB": "Bitume",
    "AC": "Fibres projetées",
    "AD": "Briquetage",
    "AE": "Grès",
    "AF": "Mortier de ciment",
    "AG": "Béton",
    "AH": "Béton armé",
    "AI": "Béton projeté",
    "AJ": "Segments de béton",
    "AK": "Fibres-ciment",
    "AL": "Plastiques renforcés de fibres",
    "AM": "Fonte",
    "AN": "Fonte grise",
    "AO": "Fonte ductile",
    "AP": "Acier",
    "AQ": "Type non identifié de fer ou d'acier",
    "AR": "Maçonnerie (appareillée)",
    "AS": "Maçonnerie (non appareillée)",
    "AT": "Époxy",
    "AU": "Polyester",
    "AV": "Polyéthylène",
    "AW": "Polypropylène",
    "AX": "PVC-U",
    "AY": "Type non identifié de plastique",
    "AZ": "Matériau non identifié",
    "Z": "Autre (avec code de remarque générale ADE)",
}

type_revetement = {
    "A": "Revêtement intégré lors de la fabrication",
    "B": "Revêtement projeté",
    "C": "Revêtement polymérisé sur place",
    "D": "Revêtements segmentaires",
    "E": "Revêtement par tuyaux discontinus",
    "F": "Revêtement par tubage continu",
    "G": "Revêtement sans espace annulaire",
    "H": "Revêtement enroulé en spirale",
    "Z": "Autre (avec code de remarque générale ADE)",
}

type_branchement = {
    "A": "Branchement ou collecteur gravitaire",
    "B": "Conduite de relèvement",
    "C": "Tuyau d'aspiration",
}

utilisation_branchement = {
    "A": "Branchement ou collecteur d'eaux usées uniquement",
    "B": "Branchement ou collecteur d'eaux de surface uniquement",
    "C": "Branchement ou collecteur de type unitaire",
    "D": "Branchement ou collecteur d'eaux usées industrielles",
    "E": "Cours d’eau en caniveau",
    "F": "Drainage souterrain ou agricole",
    "Z": "Autre (avec code de remarque générale ADE)",
}

nettoyage = {
    "A": "Le branchement ou le collecteur a été nettoyé avant l'inspection",
    "B": "Le branchement ou le collecteur n'a pas été nettoyé avant l'inspection",
}

precipitations = {
    "A": "Pas de précipitations",
    "B": "Pluie",
    "C": "Neige fondante ou glace",
}

temperature = {
    "A": "Température au-dessus de zéro",
    "B": "Température au-dessous de zéro",
}

regulation_debit = {
    "A": "Aucune mesure prise",
    "B": "L'écoulement a été obturé en amont",
    "C": "L'écoulement a été partiellement obturé en amont",
    "Z": "Autre (avec code de remarque générale ADE)",
}

observation = {
    "BAA": "Déformation",
    "BAB": "Fissure",
    "BAC": "Rupture/effondrement",
    "BAD": "Briquetage ou éléments de maçonnerie défectueux",
    "BAE": "Mortier manquant",
    "BAF": "Dégradation de surface",
    "BAG": "Branchement pénétrant",
    "BAH": "Raccordement défectueux",
    "BAI": "Joint d'étanchéité apparent",
    "BAJ": "Déplacement d'assemblage",
    "BAK": "Observations relatives au revêtement",
    "BAL": "Réparation défectueuse",
    "BAM": "Défaut de soudage",
    "BAN": "Conduite poreuse",
    "BAO": "Sol visible par le défaut",
    "BAP": "Vide visible par le défaut",
    "BBA": "Racines",
    "BBB": "Dépôts adhérents",
    "BBC": "Dépôts",
    "BBD": "Entrée de terre",
    "BBE": "Autres obstacles",
    "BBF": "Infiltration",
    "BBG": "Exfiltration",
    "BBH": "Vermine",
    "BCA": "Raccordement",
    "BCB": "Réparation ponctuelle",
    "BCC": "Courbure du collecteur",
    "BCD": "Type du noeud de départ",
    "BCE": "Référence du noeud d'arrivée",
    "BDA": "Photographie générale",
    "BDB": "Remarque générale",
    "BDC": "Inspection terminée avant le noeud d’arrivée",
    "BDD": "Niveau d'eau",
    "BDE": "Écoulement provenant d'une canalisation entrante",
    "BDF": "Atmosphère au sein de la canalisation",
    "BDG": "Perte de visibilité",
}

caracterisation_1 = {
    "BAA": {
        "A": "verticale — réduction de la conduite en hauteur",
        "B": "horizontale — réduction de la conduite en largeur",
    },
    "BAB": {
        "A": "micro-fissure — fissure présente uniquement à la surface",
        "B": "fissure fermée — ligne de fissure visible sur la paroi de la canalisation, les pièces étant toujours en place",
        "C": "fissure ouverte — fissure débouchant visiblement à la surface de la paroi de canalisation, les pièces étant toujours en place",
    },
    "BAC": {
        "A": "rupture — parties de paroi déplacées mais non manquantes",
        "B": "effondrement partiel — parties de paroi manquantes",
        "C": "effondrement — perte totale de l'intégrité structurelle",
    },
    "BAD": {
        "A": "déplacé — briques ou éléments de maçonnerie toujours présents mais déplacés par rapport à leur position initiale",
        "B": "pièces manquantes — briques ou éléments de maçonnerie manquants",
        "C": "affaissement de radier — une partie du radier d'une canalisation en briques ou en éléments de maçonnerie est descendue par rapport aux parois, laissant un vide de plus de 20 mm",
        "D": "effondrement — perte totale de l'intégrité structurelle",
    },
    "BAF": {
        "A": "rugosité accrue",
        "B": "écaillage (détachement de petits fragments de la surface)",
        "C": "granulats exposés",
        "D": "granulats déchaussés",
        "E": "granulats manquants",
        "F": "armature visible",
        "G": "armature dépassant de la surface",
        "H": "armature corrodée",
        "I": "paroi manquante",
        "J": "produits corrosifs sur la surface",
        "K": "poinçonnement (renflement interne)",
        "Z": "autre (voir remarques)",
    },
    "BAH": {
        "A": "la position du raccordement sur la canalisation est incorrecte",
        "B": "il y a un vide entre l’extrémité de la conduite de raccordement et la canalisation principale",
        "C": "il y a un vide partiel (sur une partie de la circonférence de la conduite de raccordement) entre l’extrémité de la conduite de raccordement et la canalisation principale",
        "D": "la conduite de raccordement est endommagée",
        "E": "la conduite de raccordement est obstruée",
        "Z": "autre (voir remarques)",
    },
    "BAI": {
        "A": "anneau d'étanchéité",
        "Z": "autre (voir remarques)",
    },
    "BAJ": {
        "A": "déplacement (longitudinal) — les conduites se sont déplacées parallèlement à l'axe du collecteur",
        "B": "décentrage (radial) — les conduites se sont déplacées perpendiculairement à l'axe du collecteur",
        "C": "déviation (angulaire) — les axes des canalisations ne sont pas parallèles",
    },
    "BAK": {
        "A": "le revêtement de la canalisation s’est détaché",
        "B": "décoloration du revêtement",
        "C": "extrémité du revêtement défectueuse",
        "D": "pli du revêtement",
        "E": "revêtement cloqué ou renflement interne du revêtement",
        "F": "renflement externe",
        "G": "séparation du filme interne et du revêtement",
        "H": "détachement du couvre-joint",
        "I": "fissure ou fente (y compris la rupture de soudure)",
        "J": "trou dans le revêtement",
        "K": "défaut de raccordement entre deux revêtements",
        "L": "le matériau de revêtement semble mou",
        "M": "manque de résine dans le stratifié",
        "N": "défaut d’étanchéité entre l’extrémité du revêtement et la conduite d’accueil ou le regard de visite",
        "Z": "autre (voir remarques)",
    },
    "BAL": {
        "A": "paroi manquante",
        "B": "une reprise bouchant un trou délibérément pratiqué dans la paroi de la canalisation est devenu défectueuse",
        "C": "Détachement du matériau de réparation de la conduite d'accueil",
        "D": "Matériau de réparation manquant sur la surface de contact",
        "E": "Excès de matériau de réparation constituant un obstacle",
        "F": "Trou dans le matériau de réparation",
        "G": "Fissure dans le matériau de réparation",
        "Z": "autre (voir remarques)",
    },
    "BAM": {
        "A": "longitudinale — défaut principalement parallèle à l'axe de la conduite",
        "B": "circonférentielle — défaut situé principalement sur la circonférence de la conduite",
        "C": "hélicoïdale",
    },
    "BBA": {
        "A": "grosse racine isolée",
        "B": "radicelles",
        "C": "ensemble complexe de racines",
    },
    "BBB": {
        "A": "concrétions",
        "B": "graisse",
        "C": "encrassement (par exemple, organismes attachés à la paroi de la conduite)",
        "Z": "autre (voir remarques)",
    },
    "BBC": {
        "A": "fin (par exemple, sable, vase)",
        "B": "grossier (par exemple, gravats, gravier)",
        "C": "dur ou compacté (par exemple, béton)",
        "Z": "autre (voir remarques)",
    },
    "BBD": {
        "A": "sable",
        "B": "tourbe",
        "C": "matériau fin (par exemple argile, vase)",
        "D": "gravier",
        "Z": "autre (voir remarques)",
    },
    "BBE": {
        "A": "briquetage ou élément de maçonnerie gisant sur le radier",
        "B": "fragments de conduite d’évacuation et d’assainissement gisant sur le radier",
        "C": "autre objet gisant sur le radier",
        "D": "obstacle dépassant de la paroi",
        "E": "obstacle coincé dans l'assemblage",
        "F": "obstacle traversant en provenance d’un raccordement ou une conduite de raccordement",
        "G": "conduites externes ou câbles insérés dans la canalisation",
        "H": "obstacle intégré à la structure",
        "Z": "autre (voir remarques)",
    },
    "BBF": {
        "A": "suintement — lente pénétration d'eau — aucune goutte visible",
        "B": "goutte à goutte — pénétration goutte à goutte — écoulement discontinu",
        "C": "écoulement — écoulement continu",
        "D": "jaillissement — entrée sous pression",
        "Z": "autre (voir remarques)",
    },
    "BBH": {
        "A": "rat",
        "B": "cafard",
        "Z": "autre (voir remarques)",
    },
    "BCA": {
        "A": "culotte — tuyau avec un raccord préfabriqué",
        "B": "selle — carottée — raccordement réalisé à l’aide d’une selle ou plaquette — trou net",
        "C": "selle — burinée — raccordement réalisé à l’aide d’une selle ou plaquette — trou brut",
        "D": "piquage direct — carotté — raccordement sans pièce intermédiaire — trou net",
        "E": "piquage direct — buriné — raccordement sans pièce intermédiaire — trou brut",
        "F": "raccord autre que culotte (détails manquants)",
        "G": "type de raccord inconnu",
        "Z": "autre (voir remarques)",
    },
    "BCB": {
        "A": "remplacement de la conduite",
        "B": "revêtement localisé de conduite",
        "C": "mortier injecté",
        "D": "autre matériau d’étanchéité injecté",
        "E": "trou réparé",
        "F": "revêtement localisé de raccordement (par exemple, «chapeau»)",
        "G": "autre réparation de raccordement",
        "Z": "autre (voir remarques)",
    },
    "BCC": {
        "A": "vers la gauche",
        "B": "vers la droite",
    },
    "BCD": {
        "A": "regard de visite",
        "B": "boîte d’inspection",
        "C": "orifice de nettoyage",
        "D": "orifice de passage de la lampe",
        "E": "déversoir",
        "F": "raccordement important sans regard de visite ou boîte d’inspection",
        "Z": "autre (voir remarques)",
    },
    "BCE": {
        "A": "regard de visite",
        "B": "boîte d’inspection",
        "C": "orifice de nettoyage",
        "D": "orifice de passage de la lampe",
        "E": "déversoir",
        "F": "raccordement important sans regard de visite ou boîte d’inspection",
        "Z": "autre (voir remarques)",
    },
    "BDC": {
        "A": "obstruction",
        "B": "niveau d'eau trop élevé",
        "C": "panne de l'équipement",
        "Z": "autre (voir remarques)",
    },
    "BDD": {
        "A": "claires (le radier est visible)",
        "B": "présentent un aspect discontinu",
        "C": "troubles",
        "D": "colorées",
        "E": "troubles et colorées",
    },
    "BDE": {
        "A": "clair (le radier de la canalisation entrante est visible)",
        "B": "présente un aspect discontinu",
        "C": "trouble",
        "D": "coloré",
        "E": "trouble et coloré",
        "YY": "Écoulement non visible",
    },
    "BDF": {
        "A": "manque d'oxygène",
        "B": "sulfure d'hydrogène",
        "C": "méthane",
        "Z": "autre (voir remarques)",
    },
    "BDG": {
        "A": "la caméra est sous l’eau",
        "B": "vase",
        "C": "vapeur",
        "Z": "autre (voir remarques)",
    },
}

caracterisation_2 = {
    "BAB": {
        "A": "longitudinale — fissure principalement parallèle à l'axe de la conduite",
        "B": "circonférentielle — fissure principalement située sur la circonférence de la conduite",
        "C": "complexe — groupe de fissures qui ne peuvent pas être décrites comme étant longitudinales ou circonférentielles",
        "D": "hélicoïdale",
        "E": "radiale à partir d'un point (fissure en forme d'étoile",
    },
    "BAD": {
        "A": "autre couche visible de briquetage ou d'élément de maçonnerie — par le trou laissé par le briquetage manquant",
        "B": "rien de visible — il est impossible de déterminer ce que le briquetage ou l'élément de maçonnerie manquant laisse entrevoir",
    },
    "BAF": {
        "A": "mécanique",
        "B": "chimique — générale",
        "C": "chimique — endommagement de la partie supérieure de la conduite",
        "D": "chimique — endommagement de la partie inférieure de la conduite",
        "E": "aucune cause évidente",
        "Z": "autre (voir remarques)",
    },
    "BAI": {
        "A": "visiblement déplacée mais ne dépassant pas dans la canalisation",
        "B": "pénétrant mais non rompu — point le plus bas au-dessus de la ligne médiane horizontale",
        "C": "pénétrant mais non rompu — point le plus bas au-dessous de la ligne médiane horizontale",
        "D": "pénétrant et rompu",
    },
    "BAK": {
        "A": "longitudinale",
        "B": "circonférentielle — essentiellement située sur la circonférence de la conduite",
        "C": "complexe",
        "D": "hélicoïdale",
    },
    "BAL": {
        "A": "longitudinale — essentiellement parallèle à l’axe de la conduite ;",
        "B": "circonférentielle",
        "C": "complexe",
        "D": "hélicoïdale",
    },
    "BBH": {
        "A": "dans la canalisation",
        "B": "dans un raccordement",
        "C": "dans un assemblage ouvert",
        "Z": "autre (voir remarques)",
    },
    "BCA": {"A": "raccordement ouvert", "B": "raccordement fermé"},
    "BCC": {
        "A": "vers le haut",
        "B": "vers le bas",
    },
    "BDC": {
        "A": "inspection objective terminée avant d'avoir atteint le noeud d'arrivée",
        "B": "inspection terminée sur les instructions de l'autorité responsable",
        "C": "lorsque l'on considère, par une inspection partielle précédente, que l'inspection de la conduite totale est terminée",
        "D": "lorsque l'on considère, par une inspection partielle précédente, que l'inspection de la conduite totale n'est pas terminée",
        "E": "lorsque l'on considère, par une inspection partielle précédente, que l'on ne sait pas si l'inspection de la conduite totale est terminée",
        "Z": "autre (voir remarques)",
    },
    "BDE": {
        "A": "mal raccordée car les eaux usées se déversent dans un branchement ou un collecteur d’eaux de surface",
        "B": "mal raccordée car les eaux de surface se déversent dans un branchement ou un collecteur d’eaux usées",
        "C": "aucun mauvais raccordement observé",
    },
}

unite_1 = {
    "BAA": "%",
    "BAB": "mm",
    "BAC": "mm",
    "BAD": "mm",
    "BAE": "mm",
    "BAG": "%",
    "BAI": "%",
    "BAJ": "mm",
    "BBA": "%",
    "BBB": "%",
    "BBC": "%",
    "BBD": "%",
    "BBE": "%",
    "BBH": "individus",
    "BCA": "mm",
    "BCC": "°",
    "BDD": "%",
    "BDE": "%",
}

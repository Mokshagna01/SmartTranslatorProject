from src.translation.translate import translate_paragraph

def evaluate_roundtrip(paragraph):

    print("\n===============================")
    print(" ORIGINAL ENGLISH")
    print("===============================\n")
    print(paragraph)

    # -------- Hindi round trip --------
    hindi = translate_paragraph(paragraph, "eng_Latn", "hin_Deva")
    back_en_hi = translate_paragraph(hindi, "hin_Deva", "eng_Latn")

    print("\n===============================")
    print(" HINDI TRANSLATION")
    print("===============================\n")
    print(hindi)

    print("\n===============================")
    print(" BACK TO ENGLISH (via Hindi)")
    print("===============================\n")
    print(back_en_hi)

    # -------- Telugu round trip --------
    telugu = translate_paragraph(paragraph, "eng_Latn", "tel_Telu")
    back_en_te = translate_paragraph(telugu, "tel_Telu", "eng_Latn")

    print("\n===============================")
    print(" TELUGU TRANSLATION")
    print("===============================\n")
    print(telugu)

    print("\n===============================")
    print(" BACK TO ENGLISH (via Telugu)")
    print("===============================\n")
    print(back_en_te)


if __name__ == "__main__":

    paragraph = """
    Artificial intelligence is transforming modern society at a rapid pace.
    In education, students can access personalized learning systems that adapt
    to their abilities and progress. Healthcare systems use AI to detect diseases
    early and assist doctors in making accurate diagnoses. Businesses rely on
    automation and predictive analytics to improve productivity and reduce costs.
    Governments use data-driven systems to enhance public services and planning.
    While AI creates many opportunities, it also raises concerns about privacy,
    ethics, and job displacement that must be addressed carefully.
    """

    evaluate_roundtrip(paragraph)
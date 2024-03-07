from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')  #remove ",static_url" later if i need to

# Define the scholarships database
scholarships =  [
    {
        "name": "Multiflora Garden Club Scholarship",
        "agriculture_degree": True,
        "gpa_3.0": True,
        "deadline": "March 15, 2024",
        "amount": "$1,500",
        "criteria": "Pursuing a major in horticulture (gardening), ecology, or other earth sciences; and, a cumulative non-weighted academic GPA (9-12) of 3.0 or higher.",
        "how_to_apply": "Application available with Mrs. Hanson"
    },
    {
        "name": "SLO Farm Bureau Women",
        "agriculture_degree": True,
        "deadline": "March 31, 2024",
        "amount": "$1,000",
        "criteria": "Pursuing a degree in agriculture.",
        "how_to_apply": "https://www.slofarmbureau.org/files/FBW%20Scholarship%20Application%202024.pdf"
    },
    {
        "name": "Templeton Rotary",
        "agriculture_degree": True,
        "engineering_degree": True,
        "stem_degree": True,
        "further_education": True,
        "deadline": "March 31, 2024",
        "amount": "$500-$1500",
        "criteria": "Pursuing continued education, focusing on STEM and Agriculture",
        "how_to_apply": "Application available with Mrs. Hanson"
    },
    {
        "name": "Templeton FFA Booster Scholarship",
        "ffa_member": True,
        "further_education": True,
        "deadline": "April 12, 2024",
        "amount": "$10,000",
        "criteria": "An active member of the FFA planning to continue education",
        "how_to_apply": "https://www.cognitoforms.com/CaliforniaMidStateFair1/TempletonFFAParentSupportGroupScholarshipApplication"
    },
    {
        "name": "Shelby Sudbrink Memorial Scholarship",
        "gender": "Female",
        "athlete": True,
        "deadline": "March 31, 2024",
        "amount": "$9,700",
        "criteria": "Female Athlete and exemplifies the qualities of Shelby",
        "how_to_apply": "Ask Mrs. Hanson"
    },
    {
        "name": "Templeton Presbyterian Church Academic Scholarship",
        "templeton_church_attendee": True,
        "deadline": "Coming Soon",
        "amount": "TBD",
        "criteria": "Templeton High School student that attends Templeton Presbyterian Church or participates in Templeton Presbyterian Church youth activities.",
        "how_to_apply": "Ask Mrs. Hanson"
    },
    {
        "name": "Atascadero Elks Lodge #2733 Scholarship",
        "further_education": True,
        "community_service": True,
        "deadline": "April 1, 2024",
        "amount": "Up to $1,000",
        "criteria": "Planning to continue education. Community Service, leadership, and financial need are areas of consideration",
        "how_to_apply": "Application available with Mrs. Hanson"
    },
    {
        "name": "Success Charities",
        "gpa_3.0": True,
        "community_service": True,
        "participated_community_service": True,
        "deadline": "Coming Soon",
        "amount": "$1,500",
        "criteria": "Holds a minimum non-weighted Academic GPA (9-12) of  3.0; and, demonstrates involvement in school and/or community activities or provides work history throughout their high school years",
        "how_to_apply": "Application available with Mrs. Hanson"
    },
    {
        "name": "Booker Brothers Scholarship",
        "further_education": True,
        "deadline": "April 9, 2024",
        "amount": "TBD",
        "criteria": "THS student interested in furthering their education.",
        "how_to_apply": "Application available with Mrs. Hanson"
    },
    {
        "name": "Vaqueras del Camino",
        "ffa_member": True,
        "deadline": "April 1, 2024",
        "amount": "$500",
        "criteria": "SLO County high school senior involved in 4-H or FFA.",
        "how_to_apply": "Application available with Mrs. Hanson"
    },
    {
        "name": "Templeton Women’s Charitable Club",
        "further_education": True,
        "deadline": "April 12, 2024",
        "amount": "$2,500",
        "criteria": "Templeton High School Senior planning to attend an accredited college, university, or trade school.",
        "how_to_apply": "Application available with Mrs. Hanson"
    },
    {
        "name": "American Society of Civil Engineers",
        "engineering_degree": True,
        "deadline": "Coming Soon",
        "amount": "$1,000",
        "criteria": "Graduating seniors pursuing a degree in engineering.",
        "how_to_apply": "Ask Mrs. Hanson"
    },
    {
        "name": "Hendry Fine Arts Scholarship",
        "arts_degree": True,
        "deadline": "Coming Soon",
        "amount": "$1,500",
        "criteria": "Pursuing a major/minor in the visual arts (painting, sculpture, animation, photography, ceramics, printmaking)",
        "how_to_apply": "Application available with Mrs. Hanson"
    },
    {
        "name": "Templeton Lunch Brunch Scholarship",
        "further_education": True,
        "gpa_2.5": True,
        "deadline": "April 19, 2024",
        "amount": "$500",
        "criteria": "Graduating senior from Templeton High School, minimum GPA 2.5. Plans to further their education.",
        "how_to_apply": "Application available with Mrs. Hanson"
    },
    {
        "name": "The Pat-Mar Ranch Scholarship",
        "gender": "Female",
        "agriculture_degree": True,
        "gpa_3.0": True,
        "deadline": "April 19, 2024",
        "amount": "$200",
        "criteria": "Female student currently involved in and pursuing a career in agriculture. Good grades, 3.0+ GPA, attendance, and community service.",
        "how_to_apply": "Application available with Mrs. Hanson"
    },
    {
        "name": "The Bob Miller Scholarship",
        "gender": "male",
        "agriculture_degree": True,
        "community_service": True,
        "deadline": "April 19, 2024",
        "amount": "$200",
        "criteria": "Male student currently involved in agriculture/wood shop/welding and pursuing a career in agriculture or trade industry. Good attendance and community service. Any student with a disability/challenge in life, please note their circumstance.",
        "how_to_apply": "Application available with Mrs. Hanson"
    },
    {
        "name": "THS Drama Boosters",
        "ths_drama_participant": True,
        "deadline": "Coming Soon",
        "amount": "up to $600",
        "criteria": "Graduating Seniors that participated in at least one THS Drama after-school production during senior year as either cast or crew.",
        "how_to_apply": "Coming Soon"
    },
    {
        "name": "Templeton Athletic Boosters",
        "further_education": True,
        "deadline": "April 29, 2024",
        "amount": "TBD",
        "criteria": "THS Athlete that plans to further education",
        "how_to_apply": "Ask Mrs. Hanson"
    },
    {
        "name": "Thelma Jo Sorrow Memorial Scholarship",
        "ffa_member": True,
        "ths_football_player": True,
        "deadline": "Coming Soon",
        "amount": "$300",
        "criteria": "Two scholarships are offered one for Varsity Football player and another scholarship for being active in FFA.",
        "how_to_apply": "Ask Mrs. Hanson"
    },
    {
        "name": "Templeton Teacher Association Scholarship",
        "further_education": True,
        "dei_support_involved": True,
        "deadline": "May 1, 2024",
        "amount": "$500 - $5000",
        "criteria": "SLO County student who plans to further education, actively involved in advancing social justice, equality, the celebration of diversity, and stewardship of the environment.",
        "how_to_apply": "Application available with Mrs. Hanson"
    },
    {
        "name": "Paso Robles Optimist Club",
        "further_education": True,
        "deadline": "Coming Soon",
        "amount": "$500",
        "criteria": "Templeton High School Senior planning to attend an accredited college, university or trade school.",
        "how_to_apply": "Application available with Mrs. Hanson"
    },
    {
        "name": "SLO United Methodist Church Scholarship",
        "further_education": True,
        "dei_support_involved": True,
        "deadline": "May 1, 2024",
        "amount": "$500 - $5000",
        "criteria": "SLO County student who plans to further education, actively involved in advancing social justice, equality, the celebration of diversity, and stewardship of the environment.",
        "how_to_apply": "Application available with Mrs. Hanson"
    },
    {
        "name": "Morro Bay Art Association Scholarship",
        "arts_degree": True,
        "deadline": "Coming Soon",
        "amount": "$500",
        "criteria": "Graduating senior planning to pursue a degree in visual arts is preferred, but not required.",
        "how_to_apply": "Application available with Mrs. Hanson"
    },
    {
        "name": "SLO County Quarter Horse Association",
        "equine_experience": True,
        "gpa_3.0": True,
        "deadline": "May 10, 2024",
        "amount": "$500+",
        "criteria": "SLO County high school senior with equine experience, GPA of 3.0 and higher",
        "how_to_apply": "Application available with Mrs. Hanson"
    },
    {
        "name": "Templeton Running Club",
        "ths_football_player": True,
        "deadline": "May 1, 2024",
        "amount": "$500",
        "criteria": "Graduating Senior who was a Cross Country and/or Track and Field athlete.",
        "how_to_apply": "Email: rosaliesmith@templetonrunclub.com"
    },
    {
        "name": "SLO County CattleWomen Scholarship",
        "agriculture_degree": True,
        "deadline": "April 1, 2024",
        "amount": "TBD",
        "criteria": "SLO County high school senior planning to pursue a degree in an agricultural program or related field of study",
        "how_to_apply": "https://www.cattlewomenslo.org/slo-cattlewomen-scholarship"
    },
    {
        "name": "FNL Scholarship",
        "fnl_member": True,
        "deadline": "April 12, 2024",
        "amount": "$500",
        "criteria": "SLO County high school senior, current FNL senior student and active member. Complete the online application and Letters of recommendation",
        "how_to_apply": "https://www.slofnl.com/fnl-scholarships"
    },
    {
        "name": "Lee Jeberjahn Memorial Golf Scholarship Fund",
        "financial_need": True,
        "deadline": "April 1, 2024",
        "amount": "Up to $2,000",
        "criteria": "San Luis Obispo High School. Active members of the Girls’ or Boy’s Golf Teams at San Luis Obispo High School. Demonstrated financial need.",
        "how_to_apply": "https://app.smarterselect.com/programs/90623-The-Community-Foundation-San-Luis-Obispo-County"
    },
    {
        "name": "Brian Waterbury Memorial Scholarship",
        "gpa_2.5": True,
        "deadline": "April 1, 2024",
        "amount": "Up to $10,000",
        "criteria": "High School. Graduating senior from a San Luis Obispo County high school or home school. Minimum GPA of 2.5 on a 4.0 scale. No demonstrated financial need.",
        "how_to_apply": "https://app.smarterselect.com/programs/90664-The-Community-Foundation-San-Luis-Obispo-County"
    },
    {
        "name": "Growing Up in America Art, Essay, and Video Contest",
        "arts_degree": True,
        "deadline": "March 15, 2024",
        "amount": "$1,000",
        "criteria": "Hosted by AACI and in partnership with NBC Bay Area, Growing Up in America (GUA) is an annual art, essay and video contest that reaches hundreds of Bay Area students in kindergarten through 12th grade. Founded 25+ years ago by Lance Lew of NBC Bay Area, GUA gives a unique platform for young people to creatively explore and celebrate their cultural identity through the lens of civic engagement.",
        "how_to_apply": "https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-state/california-scholarships/growing-up-in-america-art-essay-and-video-contest#"
    },
    {
        "name": "Pacific Gas & Electric Company Women's Network ERG Scholarship",
        "stem_degree": True,
        "deadline": "March 15, 2024",
        "amount": "$4,000",
        "criteria": "Employee Resource Groups not only help bring our employees together, but provide an essential bridge of communication to our customers, regardless of culture, age, gender or other defining elements. As part of the support these groups provide to the communities we serve, ERGs offer scholarship opportunities for those pursuing higher education. PG&E and its employee groups offer a wide range of scholarships to help the next generation of Californians succeed and innovate in science, technology, engineering and math (STEM), as well as other disciplines.",
        "how_to_apply": "https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-state/california-scholarships/pacific-gas-and-electric-company-womens-network-erg-scholarship"
    },
    {
        "name": "Pacific Gas & Electric Company Veterans ERG Scholarship",
        "stem_degree": True,
        "further_education": True,
        "veteran_family_member": True,
        "deadline": "March 15, 2024",
        "amount": "$5,000",
        "criteria": "Employee Resource Groups not only help bring our employees together, but provide an essential bridge of communication to our customers, regardless of culture, age, gender or other defining elements. As part of the support these groups provide to the communities we serve, ERGs offer scholarship opportunities for those pursuing higher education. PG&E and its employee groups offer a wide range of scholarships to help the next generation of Californians succeed and innovate in science, technology, engineering and math (STEM), as well as other disciplines.",
        "how_to_apply": "https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-state/california-scholarships/pacific-gas-and-electric-company-black-erg-scholarship"
    },
    {
        "name": "Pacific Gas & Electric (PG&E) Company Latino ERG Scholarship",
        "stem_degree": True,
        "further_education": True,
        "deadline": "March 15, 2024",
        "amount": "$2,000",
        "criteria": "PG&E and its employee groups offer a wide range of scholarships to help the next generation of Californians succeed and innovate in science, technology, engineering and math (STEM), as well as other disciplines. The PG&E Employee Resource Group (ERG) and Engineering Network Group (ENG) scholarships are supported by PG&E and through the fundraising and contributions of the following employee.",
        "how_to_apply": "https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-state/california-scholarships/pacific-gas-and-electric-pgande-company-latino-erg-scholarship"
    },
    {
        "name": "Fontana Transport Inc. Scholars Program",
        "first_generation_student": True,
        "further_education": True,
        "financial_need": True,
        "deadline": "March 15, 2024",
        "amount": "$5,000",
        "criteria": "The Fontana Transport Inc Scholars Program is for first generation high school seniors who are underrepresented, need financial assistance and are passionate about furthering their education as a means to help out their family, community and themselves. We want to be able to find, sponsor, and guide leaders who are determined to succeed by all means possible regardless of their struggles, lack of.",
        "how_to_apply": "https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-state/california-scholarships/fontana-transport-inc-scholars-program"
    },
    {
        "name": "Pacific Gas & Electric Company Asian ERG Scholarship",
        "stem_degree": True,
        "further_education": True,
        "deadline": "March 15, 2024",
        "amount": "$3,000",
        "criteria": "PG&E and its employee groups offer a wide range of scholarships to help the next generation of Californians succeed and innovate in science, technology, engineering and math (STEM), as well as other disciplines. The PG&E Employee Resource Group (ERG) and Engineering Network Group (ENG) scholarships are supported by PG&E and through the fundraising and contributions of the following employee",
        "how_to_apply": "https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-state/california-scholarships/pacific-gas-and-electric-company-asian-erg-scholarship"
    },
    {
        "name": "Pacific Gas & Electric Company Samahan ERG Scholarship",
        "stem_degree": True,
        "further_education": True,
        "deadline": "March 15, 2024",
        "amount": "$2,000",
        "criteria": "Employee Resource Groups not only help bring our employees together, but provide an essential bridge of communication to our customers, regardless of culture, age, gender or other defining elements. As part of the support these groups provide to the communities we serve, ERGs offer scholarship opportunities for those pursuing higher education. PG&E and its employee groups offer a wide range of scholarships to help the next generation of Californians succeed and innovate in science, technology, engineering and math (STEM), as well as other disciplines.",
        "how_to_apply": "https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-state/california-scholarships/pacific-gas-and-electric-company-samahan-erg-scholarship"
    },
    {
        "name": "Pacific Gas & Electric Company Access ERG Scholarship",
        "stem_degree": True,
        "further_education": True,
        "deadline": "March 15, 2024",
        "amount": "$3,000",
        "criteria": "Employee Resource Groups not only help bring our employees together, but provide an essential bridge of communication to our customers, regardless of culture, age, gender or other defining elements. As part of the support these groups provide to the communities we serve, ERGs offer scholarship opportunities for those pursuing higher education. PG&E and its employee groups offer a wide range of scholarships to help the next generation of Californians succeed and innovate in science, technology, engineering and math (STEM), as well as other disciplines.",
        "how_to_apply": "https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-state/california-scholarships/pacific-gas-and-electric-company-access-erg-scholarship"
    },
    {
        "name": "The Graydon & Myrth Fox Scholarship",
        "veteran_family_member": True,
        "deadline": "March 15, 2024",
        "amount": "$20,000",
        "criteria": "The Graydon and Myrth Fox Scholarship was established to assist individuals who are seeking to further their job skills or improve their circumstances through education by providing scholarships for Veterans who have served honorably in the United States Armed Forces or a surviving spouse, dependent child or grandchild of a U.S. Veteran. Preference will be given to wounded personnel.",
        "how_to_apply": "https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-state/california-scholarships/the-graydon-and-myrth-fox-scholarship"
    },
    {
        "name": "PG&E NuEnergy Scholarship",
        "stem_degree": True,
        "further_education": True,
        "deadline": "March 15, 2024",
        "amount": "$5,000",
        "criteria": " PG&E and its employee groups offer a wide range of scholarships to help the next generation of Californians succeed and innovate in science, technology, engineering and math (STEM), as well as other disciplines. The PG&E Employee Resource Group (ERG) and Engineering Network Group (ENG) scholarships are supported by PG&E and through the fundraising and contributions of the following employee.",
        "how_to_apply": "https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-state/california-scholarships/pgande-nuenergy-scholarship"
    },
    {
        "name": "AL Diablo Valley High School Scholarship",
        "gpa_3.0": True,
        "community_service": True,
        "participated_community_service": True,
        "financial_need": True,
        "further_education": True,
        "deadline": "March 20, 2024",
        "amount": "$6,000",
        "criteria": "https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-state/california-scholarships/al-diablo-valley-high-school-scholarship"
    },
    {
        "name": "FWSF Scholarship",
        "gender": True,
        "business_admin_degree": True,
        "deadline": "March 21, 2024",
        "amount": "$15,000",
        "criteria": "Undergraduate scholarships are awarded to women who will be juniors or seniors in the Fall semester of the current year. Graduate scholarships are awarded to students who will be enrolled during the upcoming Summer semester or thereafter. This includes current students or future students who have been accepted into a graduate business program.",
        "how_to_apply": "https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-state/california-scholarships/fwsf-scholarship"
    },
    {
        "name": "Executive Women International Scholarship Program",
        "further_education": True,
        "deadline": "March 25, 2024",
        "amount": "$10,000",
        "criteria": "Undergraduate scholarships are awarded to women who will be juniors or seniors in the Fall semester of the current year. Graduate scholarships are awarded to students who will be enrolled during the upcoming Summer semester or thereafter. This includes current students or future students who have been accepted into a graduate business program.",
        "how_to_apply": "https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-state/california-scholarships/executive-women-international-scholarship-program"
    },
    {
        "name": "National Organization of Black Law Enforcement Executive Region VI Scholarships",
        "further_education": True,
        "deadline": "March 29, 2024",
        "amount": "$1,000",
        "criteria": "The San Francisco Bay Area Chapter (“The Chapter”) of the National Organization of Black Law Enforcement Executives (NOBLE) seeks to enhance and advance the law enforcement profession by providing financial support to students pursuing higher education. The Chapter is pleased to offer a scholarship award of at least $1,000 to students who pursue an academic degree with the intent to work in criminal justice.",
        "how_to_apply": "https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-state/california-scholarships/national-organization-of-black-law-enforcement-executive-region-vi-scholarships"
    },
    {
        "name": "Chicana Latina Foundation Scholarships",
        "gender": True,
        "deadline": "March 31, 2024",
        "amount": "$1,500",
        "criteria": "The Chicana Latina Foundation Leadership and Scholarship Program forms the cornerstone of the Chicana Latina Foundation. Each year we award merit-based scholarships valued at $1500 to 40-45 powerful Latina students. Scholars are selected for: Commitment to equality and justice for Chicana and Latina women; Demonstrated leadership qualities and experience on behalf of the Latinx community; Clarity.",
        "how_to_apply": "https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-state/california-scholarships/chicana-latina-foundation-scholarships"
    },
    {
        "name": "SJCF Robert & Catherine Lagorio Scholarship",
        "further_education": True,
        "deadline": "March 31, 2024",
        "amount": "$5,000",
        "criteria": "Do you know a graduating high school senior in need of financial aid? We offer community-funded scholarships to eligible students with post-secondary aspirations. Awards range from hundreds to thousands of dollars and target students based on career interests and educational goals. We encourage eligible San Joaquin County high school seniors to explore and apply for the available.",
        "how_to_apply": "https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-state/california-scholarships/sjcf-robert-and-catherine-lagorio-scholarship"
    },
    ]       


def filter_scholarships(preferences, scholarships):
    matched_scholarships = []
    for scholarship in scholarships:
        criteria_matched = True
        for key, value in preferences.items():
            # Check if the preference is True and if the key exists in the scholarship
            if value and key in scholarship and not scholarship[key]:
                # If the preference is True but the scholarship criteria is False, it doesn't match
                criteria_matched = False
                break
            elif not value and key in scholarship and scholarship[key]:
                # If the preference is False but the scholarship criteria is True, it doesn't match
                criteria_matched = False
                break
        if criteria_matched:
            matched_scholarships.append(scholarship)
    return matched_scholarships

@app.route('/')
def survey():
    return render_template('survey.html')

@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    # Retrieve form data
    form_data = request.form
    print("Form Data:", form_data)

    # Update user preferences to use boolean values
    user_preferences = {key: value == 'yes' for key, value in form_data.items()}
    print("User Preferences:", user_preferences)

    # Filter scholarships based on user preferences
    matched_scholarships = filter_scholarships(user_preferences, scholarships)
    print("Matched Scholarships:", matched_scholarships)

    return render_template('matched_scholarships.html', scholarships=matched_scholarships)

if __name__ == '__main__':
    app.run(debug=True)
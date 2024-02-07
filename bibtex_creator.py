def format_author_name(names: list) -> list: 
    formatted_names = []
    for i in names:
        name_parts = i[:-2].split()   
        # Extract the last name
        last_name = name_parts[-1]
        # Extract the remaining names
        remaining_names = ' '.join(name_parts[:-1])
        # Format the name with last name first and remaining names after
        formatted_name = f"{last_name}, {remaining_names}"
        formatted_names.append(formatted_name.title())    
    return formatted_names # return a list of formatted names


def main():
    # Bibtex template
    bibtex_template = """@inproceedings{{  
        {reference_name},
        title = {{{title}}},
        author = {{{author_names}}},
        booktitle = {{Proceedings of the Fourth Workshop on Language Technology for Equality, Diversity and Inclusion}},
        month = {{March}},
        year = {{2024}},
        address = {{Malta}},
        publisher = {{European Chapter of the Association for Computational Linguistics}}
        }}"""
        
        
    reference_name = input(str("Please enter the name of the reference: "))
    title = input(str("Please enter the title of the reference: "))
    input_list = [str(x) for x in input("Enter Author names separated by comma: ").split(",")]
    author_names = format_author_name(input_list)
    author_names = ' and '.join([str(x) for x in author_names])
    bibtex = bibtex_template.format(reference_name=reference_name, title=title.strip('\''), author_names=author_names.strip('\''))
    print(bibtex) 

if __name__ == '__main__':
    main()
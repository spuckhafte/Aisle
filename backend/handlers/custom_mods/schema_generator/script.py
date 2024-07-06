"""
This script is used to create a special class for a given schema that 
provides autocompletion for supabase-table values in order to create payloads
and query strings for the "undocumented" supabase-py module

Define the required schemas in @/custom_modules/schema_generator/csg.py in the following manner:
    ~# Table
    ~field1: int
    ~field2: str
    ~field3: list[int]

    ~# Users
    ~name: str
    ~age: int
    ~tasks: list[text]

Later, run this script in terminal:
    yourmachine:~/@/custom_modules/schema_generator/ $: python script.py

Python file containing the schema class will be created: @/cs.py

Example:
    @/main.py:
        from cs import U

        insert_query = U(name="Jhon", age=3).gd() # autocompletion will be provided, gd~get_dict
        # insert_query: { "name": "Jhon", "age": 3 }
       
       select_fields = T().gk(field1=True, field3=True) # gk~get_keys
        # select_fields: "field1, field3"
"""

def __getPythonText(className: str, props: list[str], values: list[str]):
    init_param = ""
    init_inner_text = ""
    gk_param = ""
    gk_inner_text = ""
    
    i = 0
    while i < len(props):
        init_param += f"{props[i]}:{values[i]}=None, "
        init_inner_text += f"self.D_{props[i]} = {props[i]}\n\t\t"
        gk_param += f"{props[i]}=False, "
        gk_inner_text += "{" + f"'{', ' if i > 0 else ''}{props[i]}' if {props[i]} else ''" + "}"
        i += 1

    init = f"""\"\"\"{className.title()}\"\"\"\nclass {className[0].upper()}:\n\tdef __init__(self, {init_param}):\n\t\t{init_inner_text}\n\tdef gd(self, get_none=False):\n\t\t\"\"\"Generate dict from schema\"\"\"\n\t\toutput_dict = {"{}"}\n\t\tfor attr, value in vars(self).items():\n\t\t\tif attr.startswith("D_") and (get_none or value is not None):\n\t\t\t\tkeyForOutputDict = attr.split("_")[1]\n\t\t\t\toutput_dict[keyForOutputDict] = value\n\t\treturn output_dict\n\tdef gk(self, {gk_param}):\n\t\t\"\"\"Generate keys' string based on bool params\"\"\"\n\t\treturn f"{gk_inner_text}"\n\n"""
    
    return init

if __name__ == "__main__": 
    # read custom schema generator file
    csg = open("csg.py", "r")
    # write custom schema file
    cs = open("../../cs.py", "w")

    schemas = csg.read().strip().split("\n\n")

    cs_content = ""
    for schema in schemas:
        name = schema.split("# ")[1].split("\n")[0].strip()
        props, values = [], [];

        for token in schema.split("\n"):
            if token.startswith("#"):
                continue
            prop, value = token.split(":")
            props.append(prop.strip())
            values.append(value.strip() + " | " + "None")

        cs_content += __getPythonText(name, props, values)

    cs.write(cs_content);
    csg.close()
    cs.close()
    
    print("Schema(s) generated")


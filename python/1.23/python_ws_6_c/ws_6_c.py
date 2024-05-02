data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']
print(data[1]['name'])

# # 아래에 코드를 작성하시오.
for i in data:
    for z in key_list:
        i.setdefault(z, i.get(z, 'unknown'))
        print(f'{z}은/는 {i[z]}입니다.')
    print('\n')
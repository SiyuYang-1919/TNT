for comment in comments_data:
    time = comment['created_at']
    text = comment['text']
    user_id = comment['user']['id']
    user_name = comment['user'][0]['screen_name']
    user_gender = comment['user']['gender']
    user_des = comment['user']['description']
    # Other information
    url2 = user_url.format(uid=user_id)
    user_info = req.get(url2, headers=headers, timeout=10)
    root = etree.HTML(user_info.content)
    user_location = root.xpath("//div[6]/text()[4]")
    user_birth = root.xpath("//div[6]/text()[5]")
    user_other = root.xpath("//div[6]/text()[6]")

    if user_location:
        user_location = str(user_location)
    else:
        user_location = '/'

    if user_birth:
        user_birth = str(user_birth)
    else:
        user_birth = '/'
    
    if user_other:
        user_other = str(user_other)
    else:
        user_other = '/'
    
    row = [user_id, user_name, user_gender, user_birth, user_location, user_des, user_other, text, time]
    rows.append(row)
    
print('Finish!')

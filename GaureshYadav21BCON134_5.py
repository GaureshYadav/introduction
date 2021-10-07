import random
when = ['A few years ago', 'yesterday', 'last night','A long time ago','on 20th jan']
who = ['a rabbit' ,'an elephant','a mouse','a turtle','a cat']
name = ['ram','jai','veru''adi','nonu']
residence = ['Brazil','Italy','France','Germany','Europe']
went = ['cinema','university','seminar','school','laundry']
happened = ['made a lot of friends','Eats a burger','found a secret key','solved a mistery','wrote a book']
print(random.choice(when),',',random.choice(who),'that lived in',',went to the',random.choice(went),'and',random.choice(happened))

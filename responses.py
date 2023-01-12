import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'test':
        return 'Bot = Working'

    if p_message == 'roll':
        return str(random.randint(1, 12))

    if p_message == 'commands':
        return "`test - test to see if the bot is working. *roll - rolls a random number between 1 and 12. *commands - shows list of commands. what - calls brooklyn short asf. (well deserved). *size? - SillyWilly tells more about his willy. Certain emojis will aslo trigger him. *proof? - SillyWilly sends pp proof. More commands to come soon.` "
        
    if p_message == 'what':
        return '5foot1'
    
    if p_message == '<:skull:1040797049521700914>':
        return 'you are actually such a nerd, using the "skull" emoji like dude cmon'

    if p_message == '<:skul:1040797243701215252>':
        return 'what a fuckin nerd, using the skull emoji'

    if p_message == '<:emoji_6:1059585338433085501>':
        return 'bro again? go to rehab you degenerate'

    if p_message == '<:fordlarquad:1040751270157373550>':
        return 'im leaving. SillyWilly#0757 has left the server.'

    if p_message == 'size?':
        return "diameter of 12 inches, girth of 7 and a length of 15."

    if p_message == 'proof?':
        return 'https://i.pinimg.com/236x/66/78/cd/6678cd1bed9032f7431c27e81d524c6d.jpg'
        


import pygame
import os
import random
import math
from Balatro_Hand_Check import chip_calc

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Card Selection and Animation")

GUI_WIDTH = 300
GUI_PADDING = 20
GUI_BG_COLOR = (40, 40, 40)
GUI_TEXT_COLOR = (255, 255, 255)
GUI_SECTION_SPACING = 30
GUI_TITLE_FONT = pygame.font.SysFont(None, 36)
GUI_TEXT_FONT = pygame.font.SysFont(None, 24)
JOKER_WIDTH = 100
JOKER_HEIGHT = 150
JOKER_SPACING = 20
JOKER_IMAGES = []


chips = 0
previous_chips = 0
round_score = 0
multiplier = 1
ante = 1
beat = 300
current_round = 1
hands_played = 0
discards_remaining = 3
money = 0
hands = 4
potential_hand_text = ""
potential_multiplier = 0
potential_chips = 0
animation_running = False


class deck_tools:
    def __init__(self):
        self.deck = [
            ["diamonds", "cards\\2_of_diamonds.png", "2", "2", "-1"],
            ["hearts", "cards\\2_of_hearts.png", "2", "2", "-1"],
            ["spades", "cards\\2_of_spades.png", "2", "2", "-1"],
            ["clubs", "cards\\2_of_clubs.png", "2", "2", "-1"],
            ["diamonds", "cards\\3_of_diamonds.png", "3", "3", "-1"],
            ["hearts", "cards\\3_of_hearts.png", "3", "3", "-1"],
            ["spades", "cards\\3_of_spades.png", "3", "3", "-1"],
            ["clubs", "cards\\3_of_clubs.png", "3", "3", "-1"],
            ["diamonds", "cards\\4_of_diamonds.png", "4", "4", "-1"],
            ["hearts", "cards\\4_of_hearts.png", "4", "4", "-1"],
            ["spades", "cards\\4_of_spades.png", "4", "4", "-1"],
            ["clubs", "cards\\4_of_clubs.png", "4", "4", "-1"],
            ["diamonds", "cards\\5_of_diamonds.png", "5", "5", "-1"],
            ["hearts", "cards\\5_of_hearts.png", "5", "5", "-1"],
            ["spades", "cards\\5_of_spades.png", "5", "5", "-1"],
            ["clubs", "cards\\5_of_clubs.png", "5", "5", "-1"],
            ["diamonds", "cards\\6_of_diamonds.png", "6", "6", "-1"],
            ["hearts", "cards\\6_of_hearts.png", "6", "6", "-1"],
            ["spades", "cards\\6_of_spades.png", "6", "6", "-1"],
            ["clubs", "cards\\6_of_clubs.png", "6", "6", "-1"],
            ["diamonds", "cards\\7_of_diamonds.png", "7", "7", "-1"],
            ["hearts", "cards\\7_of_hearts.png", "7", "7", "-1"],
            ["spades", "cards\\7_of_spades.png", "7", "7", "-1"],
            ["clubs", "cards\\7_of_clubs.png", "7", "7", "-1"],
            ["diamonds", "cards\\8_of_diamonds.png", "8", "8", "-1"],
            ["hearts", "cards\\8_of_hearts.png", "8", "8", "-1"],
            ["spades", "cards\\8_of_spades.png", "8", "8", "-1"],
            ["clubs", "cards\\8_of_clubs.png", "8", "8", "-1"],
            ["diamonds", "cards\\9_of_diamonds.png", "9", "9", "-1"],
            ["hearts", "cards\\9_of_hearts.png", "9", "9", "-1"],
            ["spades", "cards\\9_of_spades.png", "9", "9", "-1"],
            ["clubs", "cards\\9_of_clubs.png", "9", "9", "-1"],
            ["diamonds", "cards\\10_of_diamonds.png", "10", "10", "-1"],
            ["hearts", "cards\\10_of_hearts.png", "10", "10", "-1"],
            ["spades", "cards\\10_of_spades.png", "10", "10", "-1"],
            ["clubs", "cards\\10_of_clubs.png", "10", "10", "-1"],
            ["diamonds", "cards\\jack_of_diamonds.png", "11", "10", "-1"],
            ["hearts", "cards\\jack_of_hearts.png", "11", "10", "-1"],
            ["spades", "cards\\jack_of_spades.png", "11", "10", "-1"],
            ["clubs", "cards\\jack_of_clubs.png", "11", "10", "-1"],
            ["diamonds", "cards\\queen_of_diamonds.png", "12", "10", "-1"],
            ["hearts", "cards\\queen_of_hearts.png", "12", "10", "-1"],
            ["spades", "cards\\queen_of_spades.png", "12", "10", "-1"],
            ["clubs", "cards\\queen_of_clubs.png", "12", "10", "-1"],
            ["diamonds", "cards\\king_of_diamonds.png", "13", "10", "-1"],
            ["hearts", "cards\\king_of_hearts.png", "13", "10", "-1"],
            ["spades", "cards\\king_of_spades.png", "13", "10", "-1"],
            ["clubs", "cards\\king_of_clubs.png", "13", "10", "-1"],
            ["diamonds", "cards\\ace_of_diamonds.png", "14", "11", "-1"],
            ["hearts", "cards\\ace_of_hearts.png", "14", "11", "-1"],
            ["spades", "cards\\ace_of_spades.png", "14", "11", "-1"],
            ["clubs", "cards\\ace_of_clubs.png", "14", "11", "-1"],
        ]

    def get_deck(self):
        return self.deck

    def add_to_deck(self, card):
        self.deck.append(card)

    def remove_from_deck(self, card):
        self.deck.remove(card)


class joker_tools:
    def __init__(self):
        self.jokers = []

    def get_jokers(self):
        return self.jokers

    def add_joker(self, joker):
        self.jokers.append(joker)

    def sell_joker(self, joker):
        global money
        self.jokers.remove(joker)
        money += joker[4]


jokertool = joker_tools()
jokertool.add_joker(
    joker=[
        "cards\\red_joker.png",
        "joker_code\\joker.txt",
        "card",
        0,
        0,
        "Joker",
        "+4 mult",
    ]
)
jokertool.add_joker(
    joker=[
        "cards\\red_joker.png",
        "joker_code\\joker.txt",
        "card",
        0,
        0,
        "Joker",
        "+4 mult",
    ]
)
jokers = jokertool.get_jokers()

decktool = deck_tools()
deck = decktool.get_deck()


random.shuffle(deck)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


def initialise_jokers():
    for joker in jokers:
        image = pygame.image.load(joker[0]).convert_alpha()
        scaled_image = pygame.transform.scale(image, (JOKER_WIDTH, JOKER_HEIGHT))
        JOKER_IMAGES.append(scaled_image)


initialise_jokers()


hand_size = 7

CARDS = []
cards = [deck.pop() for _ in range(hand_size)]
cards.sort(key=lambda x: int(x[2]), reverse=True)
card_count = hand_size

for card in cards:
    card_path = card[1]
    if os.path.exists(card_path):
        CARDS.append(pygame.image.load(card_path).convert_alpha())
    else:
        raise FileNotFoundError(f"Card image '{card_path}' not found!")


CARD_WIDTH = 100
CARD_HEIGHT = 150
CARDS = [pygame.transform.scale(card, (CARD_WIDTH, CARD_HEIGHT)) for card in CARDS]


def calculate_joker_positions():
    positions = []
    num_jokers = len(jokers)
    total_width = num_jokers * JOKER_WIDTH + (num_jokers - 1) * JOKER_SPACING
    start_x = (SCREEN_WIDTH - total_width) // 2

    for i in range(num_jokers):
        x = start_x + i * (JOKER_WIDTH + JOKER_SPACING)
        y = 20
        positions.append([x, y])
    return positions


def draw_joker_info(joker, pos):

    name_text = GUI_TEXT_FONT.render(joker[5], True, BLACK)
    desc_text = GUI_TEXT_FONT.render(joker[6], True, BLACK)

    name_x = pos[0] + JOKER_WIDTH // 2 - name_text.get_width() // 2
    name_y = pos[1] + JOKER_HEIGHT + 10
    desc_x = pos[0] + JOKER_WIDTH // 2 - desc_text.get_width() // 2
    desc_y = name_y + 25

    screen.blit(name_text, (name_x, name_y))
    screen.blit(desc_text, (desc_x, desc_y))


def draw_jokers():
    joker_positions = calculate_joker_positions()
    mouse_pos = pygame.mouse.get_pos()

    for i, pos in enumerate(joker_positions):

        joker_rect = pygame.Rect(pos[0], pos[1], JOKER_WIDTH, JOKER_HEIGHT)

        screen.blit(JOKER_IMAGES[i], pos)

        if joker_rect.collidepoint(mouse_pos):
            draw_joker_info(jokers[i], pos)


def draw_cards():
    for i in range(len(CARDS)):
        x, y = card_positions[i]
        screen.blit(CARDS[i], (x, y))


def draw_gui_panel(screen):
    global potential_chips, potential_multiplier
    screen.fill(WHITE)

    gui_rect = pygame.Rect(0, 0, GUI_WIDTH, SCREEN_HEIGHT)
    pygame.draw.rect(screen, GUI_BG_COLOR, gui_rect)
    
    y_pos = GUI_PADDING
    ante_text = GUI_TITLE_FONT.render(f"Score at Least:", True, GUI_TEXT_COLOR)
    screen.blit(ante_text, (GUI_PADDING, y_pos))
    beatchips_text = GUI_TITLE_FONT.render(f"{beat:,}", True, GUI_TEXT_COLOR)
    y_pos += GUI_SECTION_SPACING
    screen.blit(beatchips_text, (GUI_PADDING, y_pos))
    y_pos += GUI_SECTION_SPACING * 2

    round_text = GUI_TEXT_FONT.render("Round Score:", True, GUI_TEXT_COLOR)
    screen.blit(round_text, (GUI_PADDING, y_pos))
    score_text = GUI_TEXT_FONT.render(str(round_score), True, GUI_TEXT_COLOR)
    screen.blit(score_text, (GUI_PADDING + 120, y_pos))
    y_pos += GUI_SECTION_SPACING
    
    if selected_cards:
        potential_played_cards = []
        for card_idx in selected_cards:
            potential_played_cards.append(cards[card_idx])
            
        hand_info = chip_calc(potential_played_cards)
        potential_hand_text = hand_info[0]
        potential_hand = GUI_TEXT_FONT.render(
            f"Hand: {potential_hand_text}", True, GUI_TEXT_COLOR
        )
        screen.blit(potential_hand, (GUI_PADDING, y_pos))
        potential_multiplier = hand_info[2]
        potential_chips = hand_info[1]
        
    y_pos += GUI_SECTION_SPACING

    if animation_running:
        y_pos += GUI_SECTION_SPACING
        chips_text_words = GUI_TEXT_FONT.render(
            "chips:                  Mult:", True, GUI_TEXT_COLOR
        )
        screen.blit(chips_text_words, (GUI_PADDING, y_pos - 20))
        chips_text = GUI_TEXT_FONT.render(f"{chips}", True, GUI_TEXT_COLOR)
        screen.blit(chips_text, (GUI_PADDING, y_pos))
        mult_text = GUI_TEXT_FONT.render(f"x{multiplier}", True, GUI_TEXT_COLOR)
        screen.blit(mult_text, (GUI_PADDING + 120, y_pos))
        
    else:
        y_pos += GUI_SECTION_SPACING
        chips_text_words = GUI_TEXT_FONT.render(
            "chips:                  Mult:", True, GUI_TEXT_COLOR
        )
        screen.blit(chips_text_words, (GUI_PADDING, y_pos - 20))
        chips_text = GUI_TEXT_FONT.render(f"{potential_chips}", True, GUI_TEXT_COLOR)
        screen.blit(chips_text, (GUI_PADDING, y_pos))
        mult_text = GUI_TEXT_FONT.render(
            f"x{potential_multiplier}", True, GUI_TEXT_COLOR
        )
        screen.blit(mult_text, (GUI_PADDING + 120, y_pos))

    y_pos += GUI_SECTION_SPACING

    hands_text = GUI_TEXT_FONT.render(f"Hands: {hands}", True, GUI_TEXT_COLOR)
    screen.blit(hands_text, (GUI_PADDING, y_pos))
    discards_text = GUI_TEXT_FONT.render(
        f"Discards: {discards_remaining}", True, GUI_TEXT_COLOR
    )
    screen.blit(discards_text, (GUI_PADDING + 120, y_pos))

    y_pos += GUI_SECTION_SPACING

    money_text = GUI_TEXT_FONT.render(f"Money: ${money}", True, GUI_TEXT_COLOR)
    screen.blit(money_text, (GUI_PADDING, y_pos))
    current_ante_text = GUI_TEXT_FONT.render(f"Ante: {ante}", True, GUI_TEXT_COLOR)
    screen.blit(current_ante_text, (GUI_PADDING, y_pos + 30))

    y_pos += GUI_SECTION_SPACING
    round_text = GUI_TEXT_FONT.render(f"Round: {current_round}", True, GUI_TEXT_COLOR)
    screen.blit(round_text, (GUI_PADDING, y_pos + 30))


def calculate_card_positions():
    positions = []
    num_cards = len(CARDS)
    spacing = 20
    total_width = num_cards * CARD_WIDTH + (num_cards - 1) * spacing
    start_x = GUI_WIDTH + (SCREEN_WIDTH - GUI_WIDTH - total_width) // 2

    for i in range(num_cards):
        if num_cards > 7:

            angle = (i / (num_cards - 1) - 0.5) * math.pi * 0.5
            radius = 400
            x = start_x + radius * math.sin(angle)
            y = SCREEN_HEIGHT - radius * (1 - math.cos(angle))
        else:
            x = start_x + i * (CARD_WIDTH + spacing)
            y = SCREEN_HEIGHT - CARD_HEIGHT - 20
        positions.append([x, y])
    return positions


card_positions = calculate_card_positions()


selected_cards = []

running = True
clock = pygame.time.Clock()


button_font = pygame.font.SysFont(None, 24)
button_text = button_font.render("Play Hand", True, WHITE)
button_rect = pygame.Rect(50, SCREEN_HEIGHT - 60, 120, 40)
discard_button_text = button_font.render("Discard", True, WHITE)
discard_button_rect = pygame.Rect(50, SCREEN_HEIGHT - 120, 120, 40)


def shake_animation(image, center_pos, start_time, shake_duration, shake_steps):

    step = (pygame.time.get_ticks() - start_time) / shake_duration * shake_steps
    scale_factor = 1.0 + 0.05 * math.sin(2 * math.pi * (step / shake_steps))
    rotate_angle = 5 * math.sin(2 * math.pi * (step / shake_steps))

    transformed_image = pygame.transform.rotozoom(image, rotate_angle, scale_factor)
    image_rect = transformed_image.get_rect(center=center_pos)

    return transformed_image, image_rect


def animate_joker(joker_idx, display_text):
    shake_duration = 500
    shake_steps = 30
    start_time = pygame.time.get_ticks()
    text_duration = 2000

    if joker_idx >= len(jokers):
        return

    joker_positions = calculate_joker_positions()

    while pygame.time.get_ticks() - start_time < shake_duration:
        screen.fill(WHITE)
        draw_gui_panel(screen)
        draw_cards()

        for i, pos in enumerate(joker_positions):
            if i == joker_idx:

                joker_center = (pos[0] + JOKER_WIDTH // 2, pos[1] + JOKER_HEIGHT // 2)
                transformed_joker, joker_rect = shake_animation(
                    JOKER_IMAGES[i],
                    joker_center,
                    start_time,
                    shake_duration,
                    shake_steps,
                )
                screen.blit(transformed_joker, joker_rect)
            else:

                screen.blit(JOKER_IMAGES[i], pos)

        if display_text:
            pos = joker_positions[joker_idx]
            text = button_font.render(display_text, True, BLACK)
            text_rect = text.get_rect(
                center=(pos[0] + JOKER_WIDTH // 2, pos[1] + JOKER_HEIGHT + 20)
            )
            screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)


def animate_cards_to_center(selected_indices):
    global chips, previous_chips, multiplier, round_score, jokers, animation_running, potential_multiplier, potential_chips
    animation_running = True

    selected_cards_with_idx = [(idx, cards[idx]) for idx in selected_indices]

    selected_cards_with_idx.sort(key=lambda x: x[0])

    sorted_indices = [x[0] for x in selected_cards_with_idx]
    played_cards = [x[1] for x in selected_cards_with_idx]

    hand_type = chip_calc(played_cards)
    multiplier = hand_type[2]
    chips = hand_type[1]

    num_selected = len(sorted_indices)
    total_width = num_selected * CARD_WIDTH + (num_selected - 1) * 10
    start_x = (SCREEN_WIDTH - total_width) // 2
    target_positions = []

    for idx in range(num_selected):
        x = start_x + idx * (CARD_WIDTH + 10)
        y = (SCREEN_HEIGHT - CARD_HEIGHT) // 2
        target_positions.append((x, y))

    steps = 30
    for step in range(steps):
        screen.fill(WHITE)
        draw_gui_panel(screen)
        draw_jokers()

        for i, idx in enumerate(sorted_indices):
            current_x, current_y = card_positions[idx]
            target_x, target_y = target_positions[i]
            delta_x = (target_x - current_x) / (
                steps - step if steps - step != 0 else 1
            )
            delta_y = (target_y - current_y) / (
                steps - step if steps - step != 0 else 1
            )
            card_positions[idx][0] += delta_x
            card_positions[idx][1] += delta_y

        for i, card in enumerate(CARDS):
            x, y = card_positions[i]
            screen.blit(card, (x, y))

        pygame.display.flip()
        clock.tick(60)

    pygame.time.wait(500)
    count = 2

    repeat_shake = True

    draw_gui_panel(screen)
    pygame.time.wait(500)

    chip_font = pygame.font.SysFont(None, 36)
    for i, idx in enumerate(selected_cards_with_idx):
        idx = idx[0]

        if i in hand_type[3]:
            previous_chips = chips
            previous_mult = multiplier
            shake_duration = 500
            shake_steps = 30

            repeat_shake = True

            original_card = CARDS[idx]
            count = 0
            while repeat_shake:
                start_time = pygame.time.get_ticks()
                previous_chips = chips
                while pygame.time.get_ticks() - start_time < shake_duration:

                    step = (
                        (pygame.time.get_ticks() - start_time)
                        / shake_duration
                        * shake_steps
                    )
                    scale_factor = 1.0 + 0.05 * math.sin(
                        2 * math.pi * (step / shake_steps)
                    )
                    rotate_angle = 5 * math.sin(2 * math.pi * (step / shake_steps))

                    card_image = pygame.transform.rotozoom(
                        original_card, rotate_angle, scale_factor
                    )
                    card_rect = card_image.get_rect(
                        center=(
                            card_positions[idx][0] + CARD_WIDTH // 2,
                            card_positions[idx][1] + CARD_HEIGHT // 2,
                        )
                    )

                    screen.fill(WHITE)
                    draw_gui_panel(screen)
                    draw_jokers()

                    for j, card in enumerate(CARDS):
                        x, y = card_positions[j]
                        if j == idx:
                            screen.blit(card_image, card_rect)
                        else:
                            screen.blit(card, (x, y))

                    card_x, card_y = card_positions[idx]
                    chip_value = cards[idx][3]
                    chip_text = chip_font.render(f"+{chip_value} chips", True, BLACK)
                    text_rect = chip_text.get_rect(
                        center=(card_x + CARD_WIDTH // 2, card_y - 30)
                    )
                    screen.blit(chip_text, text_rect)
                    if chips != previous_chips + int(cards[idx][3]):
                        chips += 1

                    pygame.display.flip()
                    clock.tick(60)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()

                repeat_shake = False

                for i, joker in enumerate(jokers):
                    if joker[2] == "card":
                        joker_display_text = ""
                        local_vars = locals()

                        global_vars = globals()
                        global_vars.update(local_vars)
                        exec(open(joker[1], "r").read(), global_vars)
                        joker_display_text = global_vars["joker_display_text"]
                        globals().update(global_vars)
                        local_vars.update(locals())

                        draw_gui_panel(screen)
                        pygame.display.flip()
                        animate_joker(i, joker_display_text)
                        pygame.display.flip()

                pygame.time.wait(10)

            screen.fill(WHITE)
            draw_gui_panel(screen)
            draw_jokers()
            CARDS[idx] = original_card

            draw_cards()

            pygame.draw.rect(
                screen,
                (
                    GREEN
                    if selected_cards and animation_running != True
                    else (100, 100, 100)
                ),
                button_rect,
            )
            screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))
            pygame.draw.rect(
                screen,
                GREEN if selected_cards else (100, 100, 100),
                discard_button_rect,
            )
            screen.blit(
                discard_button_text,
                (discard_button_rect.x + 10, discard_button_rect.y + 10),
            )
            pygame.display.flip()
            draw_jokers()

    for joker in jokers:
        if joker[2] == "hand":
            joker_display_text = ""
            local_vars = locals()

            global_vars = globals()
            global_vars.update(local_vars)
            exec(open(joker[1], "r").read(), global_vars)
            joker_display_text = local_vars["joker_display_text"]
            globals().update(global_vars)

            draw_gui_panel(screen)
            draw_jokers()
            pygame.display.flip()
            animate_joker(jokers.index(joker), joker_display_text)
            pygame.display.flip()

    round_score += chips * multiplier
    draw_gui_panel(screen)
    draw_jokers()

    chips = 0
    potential_chips = 0
    potential_multiplier = 0
    multiplier = 0
    animation_running = False


def replace_selected_cards(selected_indices):

    for idx in sorted(selected_indices, reverse=True):
        cards.pop(idx)
        if len(deck) > 0:
            new_card = deck.pop()
            cards.append(new_card)
            card_path = new_card[1]
            CARDS.pop(idx)
            if os.path.exists(card_path):
                new_card_image = pygame.image.load(card_path).convert_alpha()
                new_card_image = pygame.transform.scale(
                    new_card_image, (CARD_WIDTH, CARD_HEIGHT)
                )
                CARDS.insert(idx, new_card_image)
            else:
                raise FileNotFoundError(f"Card image '{card_path}' not found!")
        else:
            CARDS.pop(idx)

    if cards:
        cards.sort(key=lambda x: int(x[2]), reverse=True)

        CARDS.clear()
        for card in cards:
            card_path = card[1]
            if os.path.exists(card_path):
                card_image = pygame.image.load(card_path).convert_alpha()
                card_image = pygame.transform.scale(
                    card_image, (CARD_WIDTH, CARD_HEIGHT)
                )
                CARDS.append(card_image)
            else:
                raise FileNotFoundError(f"Card image '{card_path}' not found!")

    global card_positions
    card_positions = calculate_card_positions()


def display_game_over_screen():
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 74)
    text = font.render("Game Over", True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)


while running:
    if not deck and not cards:
        display_game_over_screen()
        running = False
        break

    screen.fill(WHITE)
    draw_gui_panel(screen)

    mouse_pos = pygame.mouse.get_pos()
    hovered_card_index = -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button_rect.collidepoint(mouse_pos) and selected_cards and hands > 0:

                    animate_cards_to_center(selected_cards)

                    replace_selected_cards(selected_cards)
                    selected_cards.clear()
                    hands -= 1
                if (
                    discard_button_rect.collidepoint(mouse_pos)
                    and selected_cards
                    and discards_remaining > 0
                ):

                    replace_selected_cards(selected_cards)
                    selected_cards.clear()
                    discards_remaining -= 1
                else:
                    for i in range(card_count):
                        x, y = card_positions[i]
                        rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
                        if rect.collidepoint(mouse_pos):
                            if i in selected_cards:

                                selected_cards.remove(i)

                                cards[i][4] = "-1"
                            elif len(selected_cards) < 5:

                                selected_cards.append(i)
                                cards[i][4] = str(len(selected_cards) - 1)
                            screen.fill(WHITE)
                            draw_gui_panel(screen)
                            draw_jokers()
                            break

    for i in range(card_count):
        x, y = card_positions[i]
        rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        if rect.collidepoint(mouse_pos):
            hovered_card_index = i
            break

    card_count = len(CARDS)
    joker_positions = calculate_joker_positions()
    draw_jokers()

    for i in range(card_count):
        if i >= len(CARDS):
            continue

        x, y = card_positions[i]

        if i in selected_cards:
            y -= 20

        if i == hovered_card_index:
            continue

        screen.blit(CARDS[i], (x, y))

    if hovered_card_index != -1 and hovered_card_index < len(CARDS):
        x, y = card_positions[hovered_card_index]
        if hovered_card_index in selected_cards:
            y -= 20
        card = CARDS[hovered_card_index]
        enlarged_card = pygame.transform.scale(
            card, (int(CARD_WIDTH * 1.1), int(CARD_HEIGHT * 1.1))
        )
        enlarged_x = x - (enlarged_card.get_width() - CARD_WIDTH) // 2
        enlarged_y = y - (enlarged_card.get_height() - CARD_HEIGHT) // 2
        screen.blit(enlarged_card, (enlarged_x, enlarged_y))

    pygame.draw.rect(
        screen,
        GREEN if selected_cards and animation_running != True else (100, 100, 100),
        button_rect,
    )
    screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))
    pygame.draw.rect(
        screen, GREEN if selected_cards else (100, 100, 100), discard_button_rect
    )
    screen.blit(
        discard_button_text, (discard_button_rect.x + 10, discard_button_rect.y + 10)
    )

    pygame.display.flip()
    clock.tick(60)


pygame.quit()

#!/usr/bin/env python3

from pages import pages

vcoord_page = [
    [page.strip().upper() if page != '   ' else None for page in row]
    for row in pages]
page_vcoord = {page: (i, j)
               for i, row  in enumerate(vcoord_page)
               for j, page in enumerate(row)}

alphabet     = 'ABCDEFHJLMNOPRSTUVXZ'
alphabet_inv = {a: i for i, a in enumerate(alphabet)}
n_alphabet   = len(alphabet)

def vcoord_from_mapo(page, letter, number):
    page, letter = page.upper(), letter.upper()
    y, x = page_vcoord[page]

    y += (number - 0.5) / 30
    x += (alphabet_inv[letter] + 0.5) / n_alphabet
    return y, x

def mapo_from_vcoord(y, x):
    i, j = int(y), int(x)
    rest_i, rest_j = y - i, x - j

    number = int(round(rest_i * 30 + 0.5))
    letter = alphabet[int(round(rest_j * n_alphabet - 0.5))]

    return vcoord_page[i][j], letter, number

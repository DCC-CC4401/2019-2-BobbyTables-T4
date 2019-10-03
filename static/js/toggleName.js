function toggleName(id) {
    const button = $('#' + id);
    const text = button.text().replace(/(\r\n|\n|\r)/gm, '').trim();
    if (text === 'Ver más'){
        button.text('Ver menos');
    }
    else if (text === 'Ver menos'){
        button.text('Ver más');
    }
}
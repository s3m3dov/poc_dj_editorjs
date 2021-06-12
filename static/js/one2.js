var json = JSON.parse(JSON.stringify({{ content|safe }}));
var html = '';
json.blocks.forEach(function(block) {
switch (block.type) {
    case 'header':
        html += `<h${block.data.level}>${block.data.text}</h${block.data.level}>`;
        break;
    case 'paragraph':
        html += `<p>${block.data.text}</p>`;
        break;
    case 'delimiter':
        html += '<hr />';
        break;
    case 'image':
        html += `<img class="img-fluid" src="${block.data.file.url}" title="${block.data.caption}" /><br /><em>${block.data.caption}</em>`;
        break;
    case 'list':
        html += '<ul>';
        block.data.items.forEach(function(li) {
            html += `<li>${li}</li>`;
        });
        html += '</ul>';
        break;
    default:
        console.log('Unknown block type', block.type);
        console.log(block);
        break;
}
document.getElementById('article-content').innerHTML = html;
//console.log(block);
});
console.log('html: ', html);
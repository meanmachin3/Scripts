temp1.matches.map(match => match.person).filter(match => match.photos.some(photo => photo.successRate)).map(match => ({
    name: match.name,
    attractiveness: +(Math.max(...match.photos.map(photo => photo.successRate || 0)) * 10).toFixed(1)
})).sort((a, b) => b.attractiveness - a.attractiveness);

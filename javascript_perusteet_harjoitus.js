// Libraries

const mathjs = require('mathjs')

function createPersonObjekt(name, height, weight, birthDate) {
    personObject = {
        name: name,
        height: height,
        weight: weight,
        birthDate: birthDate    
    }
    return personObject
};

UlliSchmidt = createPersonObjekt('Ulli Schmidt', 179, 81, 1989);
//console.log(UlliSchmidt.name)


// Yleisempi tapa luoda objektin
class PersonObject {
    constructor(name, height, weight, birthDate) {
    this.name = name,
    this.height = height,
    this.weight = weight,
    this.birthDate = birthDate;
}
}

UllaBernstein = new PersonObject('Ulla Bernstein', 172, 68, 1993)
//console.log(UllaBernstein.height)

class Programmer {
    constructor(name, field, languages, degree, grades) {
        this.name = name;
        this.field = field;
        this.languages = languages;
        this.degree = degree;
        this.grades = grades;
    }
    averageGrades() {
        let sum = 0;
        this.grades.forEach(num => {sum += num;})
        return sum/this.grades.length;
    }
    stdDeviation() {
        let stdDev = mathjs.std(this.grades)
        return stdDev
        
    }

    }


MaxSchwerin = new Programmer('Max Schwerin', 'Backend', ['Pyton', 'Rust', 'Javascript'], 'Bachelor', [5, 4, 5, 5, 3])
JuusoOllikainen = new Programmer('Juuso Ollikainen', 'Fullstack', ['C sharp', 'SQL', 'Pyton', 'Javascript'], 'Bachelor', [4, 5, 5, 4, 3, 5, 5])
JaanaKuokka = new Programmer('Jaana Kuokka', 'Frontend', ['HTML', 'CSS', 'Javascript', 'Python'], 'Professional', [4, 4, 5, 5, 4]) 
ourProgrammers = [MaxSchwerin, JuusoOllikainen, JaanaKuokka]

/*console.log('Max Schwerin, average grade:' + MaxSchwerin.averageGrades() + '; Juuso Ollikainen, average grade:' + JuusoOllikainen.averageGrades() + 
'; Jaana Kuokka, average grade:' + JaanaKuokka.averageGrades())*/

console.log(MaxSchwerin.stdDeviation())
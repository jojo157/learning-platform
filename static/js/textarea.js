/*jshint esversion: 6 */


// Text area validation when nothing but whitespace
//credit to Sean in Tutoring
const textAreas = document.getElementsByTagName('textarea');
[...textAreas].forEach(ta => {
ta.onchange = () => {
ta.value = ta.value.trimStart();
};
});
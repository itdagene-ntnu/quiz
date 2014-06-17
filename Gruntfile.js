module.exports = function(grunt) {
  grunt.initConfig({
    sass: {
      compile: {
        files: {
          './quiz/files/static/css/base.css': 
            './quiz/files/static/css/scss/base.scss',
          './quiz/main/static/main/css/landing.css':
            './quiz/main/static/main/css/scss/landing.scss'
        }
      },
    }
  });

  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.registerTask('default', ['sass']);
};

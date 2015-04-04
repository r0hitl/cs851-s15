require "gnuplot"
require "csv"

Gnuplot.open do |gp|
  Gnuplot::Plot.new( gp ) do |plot|

    plot.terminal "png"
    plot.output File.expand_path("../plot_graph_c2.png", __FILE__)

    plot.xrange "[0:60]"
    plot.yrange "[0:60000]"
    plot.title  "Collection2"
    plot.xlabel "Word Rank"
    plot.ylabel "Word Frequency"

    words = CSV.read('after-boilerpipe.csv')

    x,y = [], []
    words.each_with_index do |word, index|
      x += [word[0]]
      y += [word[1]]
    end
    plot.data << Gnuplot::DataSet.new( [x, y] ) do |ds|
      ds.with = "linespoints"
      ds.notitle
    end
   
  end
end
puts 'plot created'


